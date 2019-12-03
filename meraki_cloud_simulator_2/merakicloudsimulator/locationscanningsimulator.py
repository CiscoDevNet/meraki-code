"""Cisco Meraki Location Scanning Data simulator"""

# Libraries
from merakicloudsimulator import merakicloudsimulator
from flask import request, render_template, redirect
import random
import datetime
from time import sleep
import requests
import threading

# module vars
location_data = ""
map_bounds = ""
client_macs = []
ap_macs = []
ap_data = []
server_url = ""
num_aps = ""

def ap_cycle(num_aps):
    ap = 0

    while True:
        print("heading to postJSON " + str(ap))
        post_json(ap)
        print("back from postJSON " + str(ap))
        determine_seen_associated()
        update_location_data(ap)
        print("back from update" + str(ap))
        print("sleeping")
        sleep(10)
        print("done sleeping")
        if ap == num_aps - 1:
            ap = 0
        else:
            ap += 1


post_location_thread = threading.Thread(target = ap_cycle,args=[num_aps], daemon=True) 

@merakicloudsimulator.route("/bounds/<map_bounds_in>", methods=["GET"])
def set_location_bounds(map_bounds_in):
    global map_bounds

    map_bounds = map_bounds_in
    map_bounds = map_bounds.replace("(", "").replace(")", "").replace(
        " ", ""
    ).split(
        ","
    )

    return ""


# generate FAKE MAC addresses for number of clients requested


def generate_client_macs(num_clients, num_aps):
    global client_macs

    for client in range(num_clients):
        client_mac = ""
        for mac_part in range(6):

            client_mac += "".join(
                random.choice("0123456789abcdef") for i in range(2)
            )

            if mac_part < 5:
                client_mac += ":"
            else:
                client_macs.append(
                    {
                        "client_mac": client_mac,
                        "associated": random.randint(0, 1),
                        "ap_associated": random.randint(1, num_aps),
                    }
                )


def determine_seen_associated():
    global client_macs
    global ap_macs

    random.shuffle(client_macs)
    random.shuffle(ap_macs)

    for client_mac in client_macs:
        client_mac["associated"] = random.randint(0, 1)
        client_mac["ap_associated"] = random.randint(1, len(ap_macs))

    for ap_mac in ap_macs:
        ap_mac["num_ap_clients_seen"] = random.randint(1, len(client_macs))


# generate FAKE MAC addresses for number of APs requested
def generate_ap_macs(num_aps, num_clients):
    global ap_macs

    for ap in range(num_aps):
        ap_mac = ""
        for mac_part in range(6):
            ap_mac += "".join(
                random.choice("0123456789abcdef") for i in range(2)
            )
            if mac_part < 5:
                ap_mac += ":"
            else:
                ap_macs.append(
                    {
                        "ap_mac": ap_mac,
                        "num_ap_clients_seen": random.randint(1, num_clients),
                    }
                )


# Kick off simulator and create baseline dataset
@merakicloudsimulator.route("/locationscanning", methods=["POST","GET"])
def generate_location_data():
    global validator
    global server_url
    global map_bounds
    global client_macs
    global ap_macs
    global ap_data
    global post_location_thread

    if request.method == "POST":
        num_clients = int(request.form["num_clients"])
        num_aps = int(request.form["num_aps"])
        server_url = request.form["server_url"]

        device_list = [
            {"os": "Android", "manufacturer": "Samsung"},
            {"os": "iOS", "manufacturer": "Apple"},
            {"os": "macOS", "manufacturer": "Apple"},
            {"os": "Windows", "manufacturer": "Lenovo"},
            {"os": "Linux", "manufacturer": "Nest"},
            {"os": "Linux", "manufacturer": "Amazon"},
        ]
        date_time_now = datetime.datetime.now()
        epoch = (
            date_time_now - datetime.datetime.utcfromtimestamp(0)
        ).total_seconds() * 1000.0

        generate_client_macs(num_clients, num_aps)
        generate_ap_macs(num_aps, num_clients)

        # generate the client distribution per ap
        # any ap may see all probing and associated clients
        # Only one ap may see an associated client
        for ap_index, ap_mac in enumerate(ap_macs):

            observations = []

            for client_index, client_mac in enumerate(client_macs):
                device = random.sample(device_list, 1)
                device = device[0]
                ipv4 = None
                ssid = None
                if client_mac["associated"] == 1 and client_mac[
                    "ap_associated"
                ] == ap_index:
                    ipv4 = "192.168.0." + str(client_index)
                    ssid = "SimulatorWifi"

                observations.append(
                    {
                        "clientMac": client_mac["client_mac"],
                        "ipv4": ipv4,
                        "ipv6": None,
                        "location": {
                            "lat": random.uniform(
                                float(map_bounds[0]), float(map_bounds[2])
                            ),
                            "lng": random.uniform(
                                float(map_bounds[1]), float(map_bounds[3])
                            ),
                            "unc": random.uniform(0, 10),
                            "x": [],
                            "y": [],
                        },
                        "manufacturer": device["manufacturer"],
                        "os": device["os"],
                        "rssi": random.randint(25, 120),
                        "seenEpoch": epoch,
                        "seenTime": date_time_now.isoformat(
                            sep="T"
                        ),
                        "ssid": ssid,
                    }
                )

            ap_data.append(
                {
                    "data": {
                        "apFloors": [],
                        "apMac": ap_mac["ap_mac"],
                        "apTags": [],
                        "observations": observations,
                    },
                    "secret": "simulator",
                    "type": "DevicesSeen",
                    "version": "2.0",
                }
            )

        # Pass the AP array to cycle through them to
        if not post_location_thread.isAlive():
            print("posting location thread not started, starting")
            post_location_thread.start() 
        else:
            print("posting thread already started, killing an restarting")
            stop_post_location_thread = True
            post_location_thread.join() 
            print('post_thread killed')
            stop_post_location_thread = False
            post_location_thread = threading.Thread(target = ap_cycle,args=[num_aps], daemon=True) 
            post_location_thread.start()

        return render_template("locationscanning.html", num_aps=num_aps, \
            num_clients=num_clients, server_url=server_url, datavar=ap_data)    
    else:
        return render_template("locationscanning.html")


def update_location_data(ap):
    global ap_data
    global map_bounds

    date_time_now = datetime.datetime.now()
    epoch = (
        date_time_now - datetime.datetime.utcfromtimestamp(0)
    ).total_seconds() * 1000.0

    ap_instance = ap_data[ap]

    observations = ap_instance["data"]["observations"]

    for observation in observations:
        observation["location"]["lat"] = random.uniform(
            float(map_bounds[0]), float(map_bounds[2])
        )
        observation["location"]["lng"] = random.uniform(
            float(map_bounds[1]), float(map_bounds[3])
        )
        observation["location"]["unc"] = random.uniform(0, 10)
        observation["rssi"] = random.randint(25, 120)
        observation["seenEpoch"] = epoch
        observation["seenTime"] = date_time_now.isoformat(
            sep="T"
        )

    ap_instance["data"]["observations"] = observations
    ap_data[ap] = ap_instance
    print("updated ap ")
    print(ap_data[ap])

def post_json(ap):
    global ap_data
    global server_url

    requests.post(server_url, json=ap_data[ap])  # post to listener
    print(ap_data[ap])


