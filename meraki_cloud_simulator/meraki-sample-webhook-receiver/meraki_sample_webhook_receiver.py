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

import env_user  # noqa
print("WT_ACCESS_TOKEN" + env_user.WT_ACCESS_TOKEN)
print("WT_ROOM_ID" + env_user.WT_ROOM_ID)

# WEBEX TEAMS LIBRARY
teamsapi = WebexTeamsAPI(access_token=env_user.WT_ACCESS_TOKEN)

# MERAKI BASE URL 
# if running in docker-compose base_url = "http://meraki_cloud_simulator:5001"
# if running seperately
base_url = "http://localhost:5001"

# Flask App
app = Flask(__name__)

# Webhook Receiver Code - Accepts JSON POST from Meraki and 
# Posts to WebEx Teams
@app.route("/", methods=["POST"])
def get_webhook_json():
    global webhook_data

    # Webhook Receiver
    webhook_data = request.json
    pprint(webhook_data, indent=1)
    webhook_data = json.dumps(webhook_data)
    # WebEx Teams can only handle so much text so limit to 1000 chars
    webhook_data = webhook_data[:1000] + '...'

    # Send Message to WebEx Teams
    teamsapi.messages.create(
        env_user.WT_ROOM_ID,
        text="Meraki Webhook Alert: " + webhook_data
    )

    # Return success message
    return "WebHook POST Received"

# Get Network ID based on Network name entry
def get_network_id(network_wh):
    orgs = ""

    # Get Orgs that entered Meraki API Key has access to
    try:
        # MISSION TODO
        orgs = requests.get(
            base_url + "/organizations",
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
                    base_url + "/organizations/"+org["id"]+"/networks",
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

# Set the Webhook receiver in Meraki
def set_webhook_receiver(network_id,url,secret,server_name):
    try:
        # MISSION TODO
        https_server_id = requests.post(
            base_url + "/networks/"+network_id+"/httpServers",
            headers = {
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            },
            data = json.dumps({
                "name" : server_name,
                "url" : url,
                "sharedSecret" : secret
            }))
        pprint(https_server_id)
        # Deserialize response text (str) to Python Dictionary object so
        # we can work with it
        https_server_id = json.loads(https_server_id.text)
        pprint(https_server_id)
        return https_server_id['id']
        # END MISSION SECTION
    except Exception as e:
        pprint(e)
        return "Setting https server fail"


# Set the Alerts in Meraki (on set 'settingsChanged')
def set_alerts(network_id,http_server_id):
    try:
        # MISSION TODO
        response = requests.put(
            base_url + "/networks/"+network_id+"/alertSettings",
            headers = {
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            },
            data = json.dumps(
                {
                    "defaultDestinations": {
                        "emails": [],
                        "snmp": False,
                        "allAdmins": False,
                        "httpServerIds": [http_server_id]
                    },
                    "alerts":[        
                                {
                                    "type": "settingsChanged",
                                    "enabled": True,
                                    "alertDestinations": {
                                        "emails": [],
                                        "snmp": False,
                                        "allAdmins": False,
                                        "httpServerIds": []
                                    },
                                    "filters": {}
                                }
                        ]
            })
        )
        pprint(response)
        return "Alerts Set Successfully"
        # END MISSION SECTION
    except Exception as e:
        pprint(e)
        return "Alert Settings Failed"

# Launch application with supplied arguments
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:s:m:", ["network=", "secret=","server_name="])
    except getopt.GetoptError:
        print("webhookreceiver.py -n network -s <secret> -m <server_name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("webhookreceiver.py -n network -s <secret> -m <server_name>")
            sys.exit()
        elif opt in ("-s", "--secret"):
            secret = arg
        elif opt in ("-n", "--network"):
            network = arg
        elif opt in ("-m", "--server_name"):
            server_name = arg

    print("secret: " + secret)
    print("network: " + network)
    print("server_name: " + server_name)
    return [network,secret,server_name]


if __name__ == "__main__":
    args = main(sys.argv[1:])

    '''
    # Code to get ngrok tunnel info so we don't have to set it manually
    # This will set our "url" value to be passed to the webhook setup
    tunnels = requests.request("GET", \
     "http://127.0.0.1:4040/api/tunnels", \
     verify=False)

    tunnels = json.loads(tunnels.text)
    tunnels = tunnels["tunnels"]

    url = ""
    for tunnel in tunnels:
        if tunnel['proto'] == 'https':
            url = tunnel['public_url']
    '''
    # If using docker-compose
    # url = "http://meraki-sample-webhook-receiver:5005"
    # If using standalone
    url = "http://localhost:5005"

    # Configuration parameters
    network_id = get_network_id(args[0])
    secret = args[1]
    server_name = args[2]
    server_id=set_webhook_receiver(network_id,url,secret,server_name)
    set_alerts(network_id,server_id)

    app.run(host="0.0.0.0", port=5005, debug=False)
