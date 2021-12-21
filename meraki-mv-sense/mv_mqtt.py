"""The provided sample code in this repository will reference this file to get the
information needed to connect to your lab backend.  You provide this info here
once and the scripts in this repository will access it as needed by the lab.
Copyright (c) 2019 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json, requests
import time
import paho.mqtt.client as mqtt
import sys, getopt
import os
from pprint import pprint
from webexteamssdk import WebexTeamsAPI

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_user  # noqa

# WEBEX TEAMS LIBRARY
teamsapi = WebexTeamsAPI(access_token=env_user.WT_ACCESS_TOKEN)

# Camera network ID, get video link
NETWORK_ID = "NETWORK ID"

# Camera serial number
CAMERA_SERIAL = "CAMERA SERIAL"

# mqtt setting
MQTT_SERVER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = "/merakimv/"+ CAMERA_SERIAL + "/0"


# motion trigger setting
MOTION_ALERT_PEOPLE_COUNT_THRESHOLD = 1

MOTION_ALERT_ITERATE_COUNT = 4

MOTION_ALERT_TRIGGER_PEOPLE_COUNT = 0

MOTION_ALERT_PAUSE_TIME = 15

_MONITORING_TRIGGERED = False

_MONITORING_MESSAGE_COUNT = 0

_MONITORING_PEOPLE_TOTAL_COUNT = 0


def collect_zone_information(topic, payload):
    parameters = topic.split("/")
    serial_number = parameters[2]
    print('SERIAL: ' + serial_number)
    zone_id = parameters[3]
    print('ZONE: ' + str(zone_id))

    # detect motion

    global _MONITORING_TRIGGERED, _MONITORING_MESSAGE_COUNT, _MONITORING_PEOPLE_TOTAL_COUNT

    # if motion monitoring triggered

    if _MONITORING_TRIGGERED:

        _MONITORING_MESSAGE_COUNT = _MONITORING_MESSAGE_COUNT + 1

        _MONITORING_PEOPLE_TOTAL_COUNT = _MONITORING_PEOPLE_TOTAL_COUNT + payload

        if _MONITORING_MESSAGE_COUNT > MOTION_ALERT_ITERATE_COUNT:

            if _MONITORING_PEOPLE_TOTAL_COUNT >= MOTION_ALERT_TRIGGER_PEOPLE_COUNT:
                # notification
                print(serial_number)
                notify(serial_number)
                # pause
                time.sleep(MOTION_ALERT_PAUSE_TIME)

            # reset
            _MONITORING_MESSAGE_COUNT = 0

            _MONITORING_PEOPLE_TOTAL_COUNT = 0

            _MONITORING_TRIGGERED = False

    if payload >= MOTION_ALERT_PEOPLE_COUNT_THRESHOLD:
        _MONITORING_TRIGGERED = True

    print("payload : " + str(payload) +
          ", _MONITORING_TRIGGERED : " + str(_MONITORING_TRIGGERED) +
          ", _MONITORING_MESSAGE_COUNT : " + str(_MONITORING_MESSAGE_COUNT) +
          ", _MONITORING_PEOPLE_TOTAL_COUNT : " + str(_MONITORING_PEOPLE_TOTAL_COUNT))


def notify(serial_number):
    # Get video link
    url = "https://api.meraki.com/api/v0/networks/{1}/cameras/{0}/snapshot".format(serial_number, NETWORK_ID)

    # current timestamp
    # ts = str(time.time()).split(".")[0] + "000"

    # querystring = {"timestamp": ts}

    print(url)
    headers = {
        'X-Cisco-Meraki-API-Key': env_user.MERAKI_API_KEY,
        "Content-Type": "application/json"
    }
    resp = requests.request("POST", url, headers=headers, json={})

    print(resp.text)
    if int(resp.status_code) == 202:
        print("trigger alert")
        msg = "An alert triggered.  \n Snapshot : {}".format(resp.json().get("url"))

        # Send Message to WebEx Teams
        teamsapi.messages.create(
            env_user.WT_ROOM_ID,
            text=msg
        )


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    payload = payload["counts"]["person"]

    collect_zone_information(msg.topic, payload)


# Get Network ID based on Network name entry
def get_network_id(network_wh):
    orgs = ""

    # Get Orgs that entered Meraki API Key has access to
    try:
        # MISSION TODO
        orgs = requests.get(
            "https://api.meraki.com/api/v0/organizations",
            headers={
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
            }
        )
        # Deserialize response text (str) to Python Dictionary object so
        # we can work with it
        orgs = json.loads(orgs.text)
        pprint(orgs)
        # END MISSION SECTION
    except Exception as e:
        pprint(e)

    # Now get a specific network based on name added on command line
    networks = ""
    if orgs != "":
        for org in orgs:
            try:
                # MISSION TODO
                networks = requests.get(
                    "https://api.meraki.com/api/v0/organizations/"+org["id"]+"/networks",
                    headers={
                        "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                    })
                # Deserialize response text (str) to Python Dictionary object so
                # we can work with it
                networks = json.loads(networks.text)
                pprint(networks)
                # END MISSION SECTION
            except Exception as e:
                pprint(e)

            for network in networks:
                if network["name"] == network_wh:
                    network_id = network["id"]
                    return network_id

    return "No Network Found with that name"

if __name__ == "__main__":
    args = sys.argv[1:]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:n:c:", ["api_key=","network=","camera="])
    except getopt.GetoptError:
        print("mv_mqtt.py -n network -c camera")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("mv_mqtt.py -n network -c camera")
            sys.exit()
        elif opt in ("-n", "--network"):
            network_wh = arg
            NETWORK_ID = get_network_id(network_wh)
        elif opt in ("-c", "--camera"):
            CAMERA_SERIAL = arg

    print("camera: " + CAMERA_SERIAL)
    print("network: " + NETWORK_ID)

    MQTT_TOPIC = "/merakimv/"+ CAMERA_SERIAL + "/0"

    # mqtt
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_SERVER, MQTT_PORT, 60)
        client.loop_forever()
    except Exception as ex:
        print("[MQTT]failed to connect or receive msg from mqtt, due to: \n {0}".format(ex))
