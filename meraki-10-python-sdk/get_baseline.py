from meraki.meraki import Meraki
import json
from pprint import pprint

# Configuration parameters and credentials for MERAKI
x_cisco_meraki_api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

client = Meraki(x_cisco_meraki_api_key)
params={}


orgs = ""
try:
    orgs = client.organizations.get_organizations()
    pprint(orgs)
except Exception as e:
    pprint(e)

# Now get a specific network
params["organization_id"] = ""
networks = ""
if orgs != "":
    for org in orgs:
        if org["name"] == "DevNet Sandbox":
            params["organization_id"] = org["id"]
            pprint(params["organization_id"])

if params["organization_id"] != "":
    try:
        networks = client.networks.get_organization_networks(params)
        pprint(networks)
    except Exception as e:
        pprint(e)

# Now get a list of devices for that network
network_id = ""
devices = ""
if networks != "":
    for network in networks:
        if network["name"] == "DevNet Always On Read Only":
            network_id = network["id"]
            pprint(network_id)

if network_id != "":
    try:
        devices = client.devices.get_network_devices(network_id)
        pprint(devices)
    except Exception as e:
        pprint(e)

