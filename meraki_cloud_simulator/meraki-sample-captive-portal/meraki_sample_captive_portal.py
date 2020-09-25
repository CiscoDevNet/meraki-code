#!/usr/bin/env python
"""External Captive Portal Web Server."""

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

import getopt
import json
import os
import sys
from pprint import pprint

import requests
from flask import Flask, json, redirect, render_template, request
from webexteamssdk import WebexTeamsAPI

import env_user  # noqa
print("WT_ACCESS_TOKEN" + env_user.WT_ACCESS_TOKEN)
print("WT_ROOM_ID" + env_user.WT_ROOM_ID)

# Module Variables
## If using docker-compose
# base_url = "http://meraki_cloud_simulator:5001"  # Using lab simulator
## If using stand alone
base_url = "http://localhost:5001"
captive_portal_base_url = "http://localhost:5004"
base_grant_url = ""
user_continue_url = ""
success_url = ""
network_id = ""

teams_api = WebexTeamsAPI(access_token=env_user.WT_ACCESS_TOKEN)

app = Flask(__name__)


# Meraki Dashboard API helper functions
# Get Network ID based on Network name entry
def get_network_id(network_name):
    """Get the network ID for a Meraki Network; searching by network name."""
    global network_id

    # Retrieve the list of organizations accessible to your API token
    # MISSION TODO
    response = requests.get(
        base_url + "/organizations",
        headers={"X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY}
    )
    # END MISSION SECTION
    response.raise_for_status()

    # Parse and print the JSON response
    orgs = response.json()
    pprint(orgs)

    # Search the organizations network lists for the network name we want
    for org in orgs:
        # MISSION TODO
        response = requests.get(
            # TODO: Add the API endpoint path to get the list of networks
            # (don't forget to add the organization ID)
            base_url + "/organizations/"+org["id"]+"/networks",
            headers={
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            },
        )
        # END MISSION SECTION
        response.raise_for_status()

        # Parse and print the JSON response
        networks = response.json()
        pprint(networks)

        for network in networks:
            if network["name"] == network_name:
                network_id = network["id"]
                return network_id


def set_splash_page_settings(network_id, captive_portal_base_url):
    """Configure the splash page settings for a network."""
    # MISSION TODO
    response = requests.put(
        # TODO: Add the API endpoint path to set the splash page settings
        # (don't forget to add the network ID)
        base_url + "/networks/"+network_id+"/ssids/0/splashSettings",
        headers={
            "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
            "Content-Type": "application/json",
        },
        json={
            "splashPage": "Click-through splash page",
            "splashUrl": captive_portal_base_url + '/click',
            "useCustomUrl": True
        },
    )
    # END MISSION SECTION
    response.raise_for_status()


def set_ssid_settings(network_id, wireless_name, wireless_password):
    """Configure an SSID to use the External Captive Portal."""
    # MISSION TODO
    response = requests.put(
        # TODO: Add the API endpoint path to set SSID settings
        # (don't forget to add the network ID)
        base_url + "/networks/"+network_id+"/ssids/0",
        headers={
            "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "number": 0,
            "name": wireless_name,
            "enabled": True,
            "splashPage": "Click-through splash page",
            "ssidAdminAccessible": False,
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
        },
    )
    # END MISSION SECTION
    response.raise_for_status()


# Flask micro-webservice URI endpoints
@app.route("/click", methods=["GET"])
def get_click():
    """Process GET requests to the /click URI; render the click.html page."""
    global base_grant_url
    global user_continue_url
    global success_url

    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac')
    success_url = host + "success"

    return render_template(
        "click.html",
        client_ip=client_ip,
        client_mac=client_mac,
        node_mac=node_mac,
        user_continue_url=user_continue_url,
        success_url=success_url,
    )


@app.route("/login", methods=["POST"])
def get_login():
    """Process POST requests to the /login URI; redirect to grant URL."""
    redirect_url = base_grant_url+"?continue_url="+success_url
    return redirect(redirect_url, code=302)


@app.route("/success", methods=["GET"])
def get_success():
    """Process GET requests to the /success URI; render success.html."""
    # MISSION TODO
    response = requests.get(
        # TODO: Add the API endpoint path to get splash page login attempts
        base_url + "/networks/"+network_id+"/splashLoginAttempts",
        headers={
            "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
            "Content-Type": "application/json"
        },
    )
    # END MISSION SECTION
    response.raise_for_status()

    # Parse JSON Data
    splash_logins = response.text
    splash_logins = json.loads(splash_logins)
    splash_logins = "```json " + json.dumps(splash_logins, indent=2)

    # Send Message to WebEx Teams
    teams_api.messages.create(
        env_user.WT_ROOM_ID,
        markdown="Splash Login Attempts:\n" + splash_logins
    )

    return render_template(
        "success.html",
        user_continue_url=user_continue_url,
    )


def parse_cli_args(argv):
    """Parse command line arguments."""
    network_name = None
    ssid_name = None
    ssid_password = None

    try:
        opts, args = getopt.getopt(
            argv,
            "hn:s:p:",
            ["network=", "ssid=", "password="],
        )
    except getopt.GetoptError:
        print(f"Usage: {__file__} -n network -s ssid -p password")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(f"Usage: {__file__} -n network -s ssid -p password")
            sys.exit()
        elif opt in ("-n", "--network"):
            network_name = arg
        elif opt in ("-s", "--ssid"):
            ssid_name = arg
        elif opt in ("-p", "--password"):
            ssid_password = arg

    if network_name and ssid_name and ssid_password:
        print("network:  " + network_name)
        print("ssid:     " + ssid_name)
        print("password: " + ssid_password)
        return network_name, ssid_name, ssid_password
    else:
        print(f"Usage: {__file__} -n network -s ssid -p password")
        sys.exit(2)


# If this script is the main being executed, configure the captive portal and
# start the web server.
if __name__ == "__main__":
    # Uncomment the following block if you are using the Meraki Cloud APIs and
    # and ngrok tunnels.

    # meraki_dashboard_api_base_url = "https://api.meraki.com/api/v0"
    # response = requests.get("http://127.0.0.1:4040/api/tunnels", verify=False)
    # response.raise_for_status()
    # tunnels = response.json()["tunnels"]
    # for tunnel in tunnels:
    #     if tunnel['proto'] == 'https':
    #         captive_portal_base_url = tunnel['public_url']

    # Parse settings from CLI arguments and configure the captive portal using
    # the Meraki Dashboard APIs.
    args = parse_cli_args(sys.argv[1:])
    network_id = get_network_id(args[0])
    ssid = args[1]
    password = args[2]
    set_ssid_settings(network_id, ssid, password)
    set_splash_page_settings(network_id, captive_portal_base_url)

    # Start the External Captive Portal web server
    app.run(host="0.0.0.0", port=5004, debug=False)
