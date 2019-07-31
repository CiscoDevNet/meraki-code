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

# Libraries
from pprint import pprint
from flask import Flask, json, request, render_template
import sys, os, getopt, json
from webexteamssdk import WebexTeamsAPI
import requests

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_user  # noqa

# WEBEX TEAMS LIBRARY
teamsapi = WebexTeamsAPI(access_token=env_user.WT_ACCESS_TOKEN)

# Flask App
app = Flask(__name__)

global base_grant_url
base_grant_url = ""
global user_continue_url
user_continue_url = ""
global success_url
success_url = ""

@app.route("/click", methods=["GET"])
def get_click():
    global base_grant_url
    global user_continue_url
    global success_url

    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac ')
    splashclick_time = request.args.get('splashclick_time')
    success_url = host + "success"

    return render_template("click.html", client_ip=client_ip,
    client_mac=client_mac, node_mac=node_mac,
    user_continue_url=user_continue_url,success_url=success_url)


@app.route("/login", methods=["POST"])
def get_login():
    global base_grant_url
    global success_url

    user_email = request.form["user_email_address"]

    return redirect(base_grant_url+"?continue_url="+success_url, code=302)

@app.route("/success",methods=["GET"])
def get_success():
    global user_continue_url

    spark.messages.create(
    env_user.WT_ROOM_ID,
    text="Succesful Splash Login"
    )

    return render_template("success.html",user_continue_url=user_continue_url)


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
                pprint(networks)
                # END MISSION SECTION
            except Exception as e:
                pprint(e)

            for network in networks:
                if network["name"] == network_wh:
                    network_id = network["id"]
                    return network_id

    return "No Network Found with that name"

def set_excap_portal(network_id,url):
    try:
        # MISSION TODO
        requests.put(
            "https://api.meraki.com/api/v0/networks/"+network_id+"/ssids/0/splashSettings",
            headers = {
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            },
            data =   {
                "splashPage": "Click-through splash page",
                "splashUrl": url+'/click',
                "useCustomUrl": True
            }
        )
        # END MISSION SECTION
    except Exception as e:
        pprint(e)

def set_ssid(network_id,wireless_name,wireless_password):
    try:
        # MISSION TODO
        requests.put(
            "https://api.meraki.com/api/v0/networks/"+network_id+"/ssids/0",
            headers = {
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            },
            data = {
                        "number": 0,
                        "name": wireless_name,
                        "enabled": True,
                        "splashPage": "Click-through splash page",
                        "ssidAdminAccessible": false,
                        "authMode": "psk",
                        "psk": wireless_password,
                        "encryptionMode": "wpa",
                        "wpaEncryptionMode": "WPA2 only",
                        "ipAssignmentMode": "Bridge mode",
                        "useVlanTagging": False,
                        "walledGardenEnabled": True,
                        "walledGardenRanges": "*.ngrok.io",
                        "minBitrate": 11,
                        "bandSelection": "5 GHz band only",
                        "perClientBandwidthLimitUp": 0,
                        "perClientBandwidthLimitDown": 0
            }
        )
        # END MISSION SECTION
    except Exception as e:
        pprint(e)

# Launch application with supplied arguments
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:s:p:", ["network=","ssid=","password="])
    except getopt.GetoptError:
        print("meraki_captive_portal.py -n network -s ssid -p password")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("meraki_captive_portal.py -n network -s ssid -p password")
            sys.exit()
        elif opt in ("-n", "--network"):
            network = arg
        elif opt in ("-s", "--ssid"):
            ssid = arg
        elif opt in ("-p", "--password"):
            password = arg

    print("ssid: " + ssid)
    print("password: " + password)
    print("network: " + network)
    return [network,ssid,password]


if __name__ == "__main__":
    args = main(sys.argv[1:])
    tunnels = requests.request("GET", \
     "http://127.0.0.1:4040/api/tunnels", \
     verify=False)

    tunnels = json.loads(tunnels.text)
    tunnels = tunnels["tunnels"]

    url = ""
    for tunnel in tunnels:
        if tunnel['proto'] == 'https':
            url = tunnel['public_url']

    # Configuration parameters
    network_id = get_network_id(args[0])
    ssid = args[1]
    password = args[2]
    set_ssid(network_id,ssid,password)
    set_excap_portal(network_id,url)

    app.run(host="0.0.0.0", port=5004, debug=False)
