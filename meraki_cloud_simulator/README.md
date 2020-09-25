# Meraki Cloud Simulator
Locally run Python 3.5+ Flask based application that provides HTTP POST simulations of Location Scanning, WebHook Alerts and Splash Page (Captive Portal) Integrations.

The simulator can be run as a standalone python application or as Docker container in conjunction with all supporting samples (location scanning, webhook alerts, and captive portal).

* [Run as Docker Container](#Run-as-Docker-Container)
* [Run as Python Standalone](#Run-as-Python-Standalone)

## Run as Docker Container

The webhook simulator and the captive portal simulator use Webex Teams to post updates.  Before starting the application, add in your developer token and room ID  (see: https://developer.webex.com) that you'd like to post notifications to.  Those are added in the wt_vars.env file and will be pulled into the appropriate containters.  You can then start all containers with:

```
docker-compose build
docker-compose up
```

This will build and run four containers:

* The simulator itself: web address is http://localhost:5001/go and will take you to a menu of available simulations
* A sample location scanning receiver: web address is http://localhost:5002/go but in the container network it is identified as http://meraki-sample-location-scanning-receiver:5002.  See [Sample Location Scanning Receiver](#Sample-Location-Scanning-Receiver) for instruction on use.
* A sample webhook alert receiver: see [Sample Webhook Alert Receiver](#Sample-Webhook-Alert-Receiver) for instruction on use.
* A sample captive portal: see [Sample Captive Portal](#Sample-Captive-Portal) for instruction on use.


Head to http://localhost:5001/go to validate simulator is up and running and select the simulation you'd like to run (you can run all three at the same time).


## Run as Python Standalone
This simulator can also be run as a standalone Python web service without using docker-compose.  In this instance, the simulator and all samples will need to be started independently OR samples can be replaced with your custom applications.

To run the simulator:

* virtual envrionment:
```
python3 -m venv simulator
source simulator/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Go!
```
python meraki_cloud_simulator.py
```

Navigate to http://localhost:5001/go and select the simulator you'd like to use.


## Sample Location Scanning Receiver

### If running with docker-compose

Navigate to http://localhost:5002/go to verify sample receiver is up and running.

Navigate to http://localhost:5001/go and select Location Scanning Simulator.  Enter number of clients and APs for the simulator provide location data, set the location of the desired map and the receiving services url to http://meraki-sample-location-scanning-receiver:5002 and hit Launch Simulator to run.  Location data for that location, AP and client set will be generated sent to the receiver.  To see updated locations navigate to http://localhost:5002/go and see blue dots for simulated device locations.

### If running as a Python standalone service with simulator sending data

This sample can be run as a python standalone service as well.  Use this if you're running the simulator as a standalone Python application.

* virtual envrionment:
```
python3 -m venv location_receiver
source location_receiver/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Go!
```
python meraki_sample_location_scanning_receiver.py -v simulator -s simulator
```

### If running as a Python standalone service with your Meraki organization sending data

This sample can be also used to collect data from the live Meraki platform rather than the simulator.  If you are an administrator in a Meraki organization you can do the following.

1. Navigate to the [Meraki Dashboard](https://meraki.cisco.com). Login with your username and password
1. On the left rail, click on the **Networks** drop-down and make sure to choose the desired network. This changes the context to the network to which you'll configure the location scanning.
1. Under **Network**, select **Network-wide->General**.
1. Scroll down to **Location and Scanning** and verify the API is enabled.
1. Copy the validator key

* virtual envrionment:
```
python3 -m venv location_receiver
source location_receiver/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Go!
```
python meraki_sample_location_scanning_receiver.py -v <validator copied from Meraki dashboard> -s <desired shared secret>
```

* Expose service using ngrok
```
ngrok http 5002
```

This will allow your service to be accessible to the public internet for testing.

1. Navigate to the [Meraki Dashboard](https://meraki.cisco.com). Login with your username and password
1. On the left rail, click on the **Networks** drop-down and make sure to choose the desired network. This changes the context to the network to which you'll configure the location scanning.
1. Under **Network**, select **Network-wide->General**.
1. Scroll down to **Location and Scanning** and verify the API is enabled.
1. Update publicly accessible url of the receiving application with the url generated from the **ngrok** tool in the **Post URL** and set the **Secret** to the same value you used to launch your receiver above.
1. Click **Validate** to verify connectivity.
1. If your server validates, then Meraki can send the `HTTPS POST` data to it.
1. Scroll to the bottom and click **Save** in the lower right corner.


## Sample Webhook Alert Receiver

### If running with docker-compose

Navigate to http://localhost:5001/go and select Webhook Alerts Simulator.  Select the desired alerts to collect and at the bottom fill out the 

### If running as a Python standalone service with simulator sending data

This sample can be run as a python standalone service as well.  Use this if you're running the simulator as a standalone Python application.


### If running as a Python standalone service with your Meraki organization sending data


## Captive portal

Enter the URL for the captive portal to be tested and the continuation URL.  Upon hitting "Simulate WiFi Connection" the service will open a new tab to the captive portal as if your local client was connecting to a Meraki SSID and serving up a captive portal
