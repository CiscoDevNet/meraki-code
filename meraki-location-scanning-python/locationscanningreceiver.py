#!flask/bin/python

"""
Cisco Meraki Location Scanning Receiver

The provided sample code in this repository will reference this file to get the
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
from flask import Flask
from flask import json
from flask import request
from flask import render_template
import sys, getopt
import json

############## USER DEFINED SETTINGS ###############
# MERAKI SETTINGS
validator = "EnterYourValidator"
secret = "EnterYourSecret"
version = "2.0" 
locationdata = "Location Data Holder"
####################################################
app = Flask(__name__)


# Respond to Meraki with validator


@app.route("/", methods=["GET"])
def get_validator():
    print("validator sent to: ", request.environ["REMOTE_ADDR"])
    return validator


# Accept CMX JSON POST


@app.route("/", methods=["POST"])
def get_locationJSON():
    global locationdata

    if not request.json or not "data" in request.json:
        return ("invalid data", 400)

    locationdata = request.json
    pprint(locationdata, indent=1)
    print("Received POST from ", request.environ["REMOTE_ADDR"])

    # Verify secret
    if locationdata["secret"] != secret:
        print("secret invalid:", locationdata["secret"])
        return ("invalid secret", 403)

    else:
        print("secret verified: ", locationdata["secret"])

    # Verify version
    if locationdata["version"] != version:
        print("invalid version")
        return ("invalid version", 400)

    else:
        print("version verified: ", locationdata["version"])

    # Determine device type
    if locationdata["type"] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif locationdata["type"] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")
        return ("invalid device type", 403)

    # Return success message
    return "Location Scanning POST Received"


@app.route("/go", methods=["GET"])
def get_go():
    return render_template("index.html", **locals())


@app.route("/clients/", methods=["GET"])
def get_clients():
    global locationdata
    if locationdata != "Location Data Holder":
        # pprint(locationdata["data"]["observations"], indent=1)
        return json.dumps(locationdata["data"]["observations"])

    return ""


@app.route("/clients/<clientMac>", methods=["GET"])
def get_individualclients(clientMac):
    global locationdata
    for client in locationdata["data"]["observations"]:
        if client["clientMac"] == clientMac:
            return json.dumps(client)

    return ""


# Launch application with supplied arguments


def main(argv):
    global validator
    global secret

    try:
        opts, args = getopt.getopt(argv, "hv:s:", ["validator=", "secret="])
    except getopt.GetoptError:
        print("locationscanningreceiver.py -v <validator> -s <secret>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("locationscanningreceiver.py -v <validator> -s <secret>")
            sys.exit()
        elif opt in ("-v", "--validator"):
            validator = arg
        elif opt in ("-s", "--secret"):
            secret = arg

    print("validator: " + validator)
    print("secret: " + secret)


if __name__ == "__main__":
    main(sys.argv[1:])
    app.run(host="0.0.0.0", port=5002, debug=False)
