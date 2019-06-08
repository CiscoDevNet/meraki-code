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

# Libraries
from pprint import pprint
from flask import Flask
from flask import json
from flask import request
from flask import render_template
import sys, getopt
import os
import sys
import ciscosparkapi
import requests
from meraki.meraki import Meraki
import json
from pprint import pprint
from meraki.models.create_network_http_servers_model import (
    CreateNetworkHttpServersModel
)
from meraki.models.create_network_http_servers_webhook_tests_model import (
    CreateNetworkHttpServersWebhookTestsModel
)
from meraki.models.update_network_alert_settings_model import (
    UpdateNetworkAlertSettingsModel
)
from meraki.models.default_destinations_model import (
    DefaultDestinationsModel
)
from meraki.models.alert_model import (
    AlertModel
)
from meraki.exceptions.api_exception import APIException

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_user  # noqa


# Create a Cisco Spark object
spark = ciscosparkapi.CiscoSparkAPI(access_token=env_user.WT_ACCESS_TOKEN)

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
    webhook_data = webhook_data[:1000] + '...'

    # Send Message to WebEx Teams
    spark.messages.create(
        env_user.WT_ROOM_ID,
        text="Meraki Webhook Alert: " + webhook_data
    )

    # Return success message
    return "WebHook POST Received"

# Get Network ID based on Network name entry
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

# Set the Webhook receiver in Meraki
def set_webhook_receiver(network_id,url,secret,server_name):
    try:
        collect = {}
        collect['network_id'] = network_id

        create_network_http_servers = CreateNetworkHttpServersModel()
        create_network_http_servers.name = server_name
        create_network_http_servers.url = url
        create_network_http_servers.shared_secret = secret
        # MISSION TODO
        collect['create_network_http_servers'] = create_network_http_servers

        result = # MISSION - fill in the Python SDK code to create the https receiving server
        print("Webhook Server Set Succesfully")
        # END MISSION
        return result['id']
    except APIException as e:
        print(e)
        print(e.response_code)
        return "Setting https server fail"


# Set the Alerts in Meraki (on set 'settingsChanged')
def set_alerts(network_id,http_server_id):
    try:
        collect = {}
        collect['network_id'] = network_id

        update_network_alert_settings = UpdateNetworkAlertSettingsModel()
        update_network_alert_settings.default_destinations = DefaultDestinationsModel()
        update_network_alert_settings.default_destinations.http_server_ids = [http_server_id]
        update_network_alert_settings.default_destinations.all_admins = False
        update_network_alert_settings.default_destinations.snmp = False
        update_network_alert_settings.alerts = []

        update_network_alert_settings.alerts.append(AlertModel())
        update_network_alert_settings.alerts[0].mtype = 'settingsChanged'
        update_network_alert_settings.alerts[0].enabled = True

        # MISSION TODO
        collect['update_network_alert_settings'] = update_network_alert_settings

        result = # MISSION - fill in the Python SDK code to Update Network Alert Settings
        # END MISSION
        print("Alerts Set Successfully")
    except APIException as e:
        print(e)
        print(e.response_code)
        return "Setting Alerts Fail"


# Launch application with supplied arguments
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:n:s:m:", ["api_key=","network=", "secret=","server_name="])
    except getopt.GetoptError:
        print("webhookreceiver.py -a api_key -n network -s <secret> -m <server_name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("webhookreceiver.py -a api_key -n network -s <secret> -m <server_name>")
            sys.exit()
        elif opt in ("-s", "--secret"):
            secret = arg
        elif opt in ("-n", "--network"):
            network = arg
        elif opt in ("-a", "--api_key"):
            api_key = arg
        elif opt in ("-m", "--server_name"):
            server_name = arg

    print("secret: " + secret)
    print("network: " + network)
    print("api_key: " + api_key)
    print("server_name: " + server_name)
    return [network,secret,api_key,server_name]


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
    x_cisco_meraki_api_key = args[2]

    # MISSION TODO
    client = # MISSION - instatiate the Meraki class to use the Python SDK
    network_id = get_network_id(args[0])
    secret = args[1]
    server_name = args[3]
    server_id=set_webhook_receiver(network_id,url,secret,server_name)
    set_alerts(network_id,server_id)
    # END MISSION

    app.run(host="0.0.0.0", port=5005, debug=False)