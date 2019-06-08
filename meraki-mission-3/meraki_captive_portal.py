"""The provided sample code in this repository will reference this file to get the
information needed to connect to your lab backend.  You provide this info here
once and the scripts in this repository will access it as needed by the lab.
Copyright (c) 2018 Cisco and/or its affiliates.
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

from pprint import pprint
from flask import Flask, request, render_template, redirect, url_for, json
import sys, getopt
import json
import ciscosparkapi
import sys, getopt
import os
import sys
import ciscosparkapi
import requests

from meraki.meraki import Meraki
# Object Model for Networks
from meraki.models.update_network_ssids_plash_settings_model import (
   UpdateNetworkSsidsPlashSettingsModel
)
from meraki.models.update_network_ssid_model import (
    UpdateNetworkSsidModel
)
from meraki.models.ap_tags_and_vlan_id_model import (
    ApTagsAndVlanIdModel
)
from meraki.models.radius_accounting_server_model import (
    RadiusAccountingServerModel
)
from meraki.models.radius_server_model import (
    RadiusServerModel
)
from meraki.exceptions.api_exception import APIException

app = Flask(__name__)

global base_grant_url
base_grant_url = ""
global user_continue_url
user_continue_url = ""
global success_url
success_url = ""


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_user  # noqa


# Create a Cisco Spark object
spark = ciscosparkapi.CiscoSparkAPI(access_token=env_user.WT_ACCESS_TOKEN)


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


def get_network_id(network_wh):
    params={}
    orgs = ""

    # Get Orgs that entered Meraki API Key has access to
    try:
        # MISSION TODO
        orgs = # MISSION - add in Python SDK call to get list of organizations
        pprint(orgs)
    except Exception as e:
        pprint(e)
        # END MISSION
    # Now get a specific network based on name added on command line
    params["organization_id"] = ""
    networks = ""
    if orgs != "":
        for org in orgs:
            params["organization_id"] = org["id"]
            pprint(params["organization_id"])

            if params["organization_id"] != "":
                try:
                    # MISSION TODO
                    networks = # MISSION - add in Python SDK Call to get list of networks
                    pprint(networks)
                except Exception as e:
                    pprint(e)
                    # END MISSION

                for network in networks:
                    if network["name"] == network_wh:
                        network_id = network["id"]
                        return network_id

def set_excap_portal(network_id,url):
    try:
        collect = {}
        collect['network_id'] = network_id
        
        number = '0'
        collect['number'] = number
        
        update_network_ssids_plash_settings = UpdateNetworkSsidsPlashSettingsModel()
        update_network_ssids_plash_settings.splash_url = url+'/click'
        update_network_ssids_plash_settings.use_splash_url = True
        collect['update_network_ssids_plash_settings'] = update_network_ssids_plash_settings
        
        # MISSION TODO 
        result = # MISSION - fill in the Python SDK code to set splash page settings
        # END MISSION
    except Exception as e:
        print(e)

def set_ssid(network_id,wireless_name,wireless_password):
    try:
        collect = {}
        collect['network_id'] = network_id

        number = '0'
        collect['number'] = number

        update_network_ssid = UpdateNetworkSsidModel()
        update_network_ssid.name = wireless_name
        update_network_ssid.enabled = True
        update_network_ssid.auth_mode = 'psk'
        update_network_ssid.encryption_mode = 'wpa'
        update_network_ssid.psk = wireless_password
        update_network_ssid.wpa_encryption_mode = 'WPA2 only'
        update_network_ssid.splash_page = 'Click-through splash page'
        update_network_ssid.ip_assignment_mode = 'Bridge mode'
        update_network_ssid.use_vlan_tagging = False
        update_network_ssid.concentrator_network_id = network_id
        update_network_ssid.radius_accounting_enabled = False
        update_network_ssid.radius_servers = []

        update_network_ssid.radius_servers.append(RadiusServerModel())
        update_network_ssid.radius_servers[0].host = '0.0.0.0'
        update_network_ssid.radius_servers[0].port = '22'
        update_network_ssid.radius_servers[0].secret = 'booyah'

        update_network_ssid.radius_accounting_servers = []


        update_network_ssid.radius_accounting_servers.append(RadiusAccountingServerModel())
        update_network_ssid.radius_accounting_servers[0].host = '0.0.0.0'
        update_network_ssid.radius_accounting_servers[0].port = '22'
        update_network_ssid.radius_accounting_servers[0].secret = 'booyah'


        update_network_ssid.ap_tags_and_vlan_ids = []

        update_network_ssid.ap_tags_and_vlan_ids.append(ApTagsAndVlanIdModel())
        update_network_ssid.ap_tags_and_vlan_ids[0].tags = 'wireless'
        update_network_ssid.ap_tags_and_vlan_ids[0].vlan_id = '2'

        update_network_ssid.walled_garden_enabled = True
        update_network_ssid.walled_garden_ranges = '*.amazon.aws.com'
        update_network_ssid.min_bitrate = '11'
        update_network_ssid.band_selection = '5 GHz band only,'
        update_network_ssid.per_client_bandwidth_limit_up = '0'
        update_network_ssid.per_client_bandwidth_limit_down = '0'
        collect['update_network_ssid'] = update_network_ssid
        # MISSION TODO
        result = # MISSION - fill in Python SDK code to update a wireless SSID
        # END MISSION
    except Exception as e:
        print(e)

# Launch application with supplied arguments
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:n:s:p:", ["api_key=","network=","ssid=","password="])
    except getopt.GetoptError:
        print("meraki_captive_portal.py -a api_key -n network -s ssid -p password")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("meraki_captive_portal.py -a api_key -n network -s ssid -p password")
            sys.exit()
        elif opt in ("-n", "--network"):
            network = arg
        elif opt in ("-s", "--ssid"):
            ssid = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-a", "--api_key"):
            api_key = arg

    print("ssid: " + ssid)
    print("password: " + password)
    print("network: " + network)
    print("api_key: " + api_key)
    return [network,ssid,password,api_key]


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

    # Configuration parameters and credentials for MERAKI
    x_cisco_meraki_api_key = args[3]

    # MISSION TODO 
    client = # MISSION - Instantiate the Meraki Python SDK with the Meraki API Key
    # END MISSION
    network_id = get_network_id(args[0])
    ssid = args[1]
    password = args[2]
    set_ssid(network_id,ssid,password)
    set_excap_portal(network_id,url)

    app.run(host="0.0.0.0", port=5004, debug=False)