#!/usr/bin/env python
"""Cisco Meraki Cloud Simulator for External Captive Portal labs."""

import random
from datetime import datetime

from flask import abort, Flask, jsonify, redirect, render_template, request


# Module Constants & Simulated Cloud Data
WEB_SERVER_HOSTNAME = "localhost"
WEB_SERVER_BIND_IP = "0.0.0.0"
WEB_SERVER_BIND_PORT = 5003

ORGANIZATIONS = [{"id": "1234567", "name": "Simulated Organization"}]

# Networks indexed by organization ID.
NETWORKS = {
    "1234567": [
        {
            "id": "L_12345678910",
            "organizationId": "1234567",
            "name": "Simulated Network",
            "timeZone": "America/New_York",
            "tags": "",
            "productTypes": ["appliance", "switch", "wireless"],
            "type": "combined",
            "disableMyMerakiCom": False,
            "disableRemoteStatusPage": True,
        },
    ]
}


# Module Variables
captive_portal_url = ""
user_continue_url = ""
window = ""
splash_logins = []

app = Flask(__name__)


# Helper Functions
def generate_fake_mac():
    """Generate a fake MAC address."""
    hex_characters = "0123456789abcdef"

    def random_byte():
        """Generate a random byte."""
        return random.choice(hex_characters) + random.choice(hex_characters)

    return ":".join(random_byte() for _ in range(6))


# Flask micro-webservice API/URI endpoints
@app.route("/organizations", methods=["GET"])
def get_org_id():
    """Get a list of simulated organizations."""
    return jsonify(ORGANIZATIONS)


@app.route("/organizations/<organization_id>/networks", methods=["GET"])
def get_networks(organization_id):
    """Get the list of networks for an organization."""
    organization_networks = NETWORKS.get(organization_id)
    if organization_networks:
        return jsonify(organization_networks)
    else:
        abort(404)


@app.route("/networks/<network_id>/ssids/<ssid_id>", methods=["PUT"])
def put_ssid(network_id, ssid_id):
    """Simulate setting SSID configurations."""
    print(f"Settings updated for network {network_id} ssid {ssid_id}.")
    return jsonify(request.json)


@app.route(
    "/networks/<network_id>/ssids/<ssid_id>/splashSettings",
    methods=["PUT"],
)
def put_splash(network_id, ssid_id):
    """Simulate setting Splash Page configurations."""
    print(f"Splash settings updated for network {network_id} ssid {ssid_id}.")
    return jsonify(request.json)


@app.route("/networks/<network_id>/splashLoginAttempts", methods=["GET"])
def get_splash_logins(network_id):
    """Get list of Splash Page logins."""
    # We aren't associating specific logins with a network ID
    _ = network_id
    return jsonify(splash_logins)


@app.route("/go", methods=["GET"])
def get_go():
    """Process GET requests to the /go URI; render the index.html page."""
    return render_template("index.html")


@app.route("/connecttowifi", methods=["POST"])
def connect_to_wifi():
    """Save captive portal details; redirect to the External Captive Portal."""
    global captive_portal_url
    global user_continue_url
    global splash_logins

    captive_portal_url = request.form["captive_portal_url"]
    base_grant_url = request.host_url + "splash/grant"
    user_continue_url = request.form["user_continue_url"]
    node_mac = generate_fake_mac()
    client_ip = request.remote_addr
    client_mac = generate_fake_mac()
    splash_click_time = datetime.utcnow().isoformat()
    full_url = (
        captive_portal_url
        + "?base_grant_url=" + base_grant_url
        + "&user_continue_url=" + user_continue_url
        + "&node_mac=" + node_mac
        + "&client_ip=" + client_ip
        + "&client_mac=" + client_mac
    )

    splash_logins.append(
        {
            "name": "Simulated Client",
            "login": "simulatedclient@meraki.com",
            "ssid": "Simulated SSID",
            "loginAt": splash_click_time,
            "gatewayDeviceMac": node_mac,
            "clientMac": client_mac,
            "clientId": client_ip,
            "authorization": "success",
        }
    )

    return redirect(full_url, code=302)


@app.route("/splash/grant", methods=["GET"])
def continue_to_url():
    """Accept captive portal click-through; redirect to the continue URL."""
    return redirect(request.args.get("continue_url"), code=302)


if __name__ == "__main__":
    print(
        f"\n>>> "
        f"Open your browser and browse to "
        f"http://{WEB_SERVER_HOSTNAME}:{WEB_SERVER_BIND_PORT}/go "
        f"to configure the captive portal and simulate a client login."
        f" <<<\n"
    )

    # Start the web server
    app.run(host=WEB_SERVER_BIND_IP, port=WEB_SERVER_BIND_PORT, debug=False)
