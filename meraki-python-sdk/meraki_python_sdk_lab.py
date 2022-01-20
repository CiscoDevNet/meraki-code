import meraki
import json
from pprint import pprint

# Configuration parameters and credentials for MERAKI
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

client = meraki.DashboardAPI(api_key=API_KEY)
params={}


orgs = ""
try:
    orgs = client.organizations.getOrganizations()
    pprint(orgs)
except Exception as e:
    pprint(e)

params["organization_id"] = ""
networks = ""
if orgs != "":
    for org in orgs:
        if org["name"] == "DevNet Sandbox":
            params["organization_id"] = org["id"]
            pprint(params["organization_id"])

if params["organization_id"] != "":
    try:
        networks = client.organizations.getOrganizationNetworks(params["organization_id"])
        pprint(networks)
    except Exception as e:
        pprint(e)

# Now get a list of devices for that network
network_id = ""
devices = ""
if networks != "":
    for network in networks:
        if network["name"] == "DevNet Sandbox ALWAYS ON":
            network_id = network["id"]
            pprint(network_id)

if network_id != "":
    try:
        devices = client.networks.getNetworkDevices(network_id)
        pprint(devices)
    except Exception as e:
        pprint(e)