#!/usr/bin/env python
"""External Captive Portal Web Server."""

from flask import Flask, redirect, render_template, request


# Module Variables
base_grant_url = ""
user_continue_url = ""
success_url = ""

app = Flask(__name__)


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
    global user_continue_url

    return render_template(
        "success.html",
        user_continue_url=user_continue_url,
    )


# If this script is the main script being executed, start the web server.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=False)
