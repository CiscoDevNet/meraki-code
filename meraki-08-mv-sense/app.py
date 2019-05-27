import json, requests
import time
import paho.mqtt.client as mqtt

from webexteam import sent_notification

# mqtt setting
MQTT_SERVER = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/merakimv/Q2GV-Y4MD-VSQ6/0"

# Meraki api key
MERAKI_API_KEY = "dc4f4ae03d125032313568a55ca22eaeaf078ff6"

# Camera network ID, get video link
NETWORK_ID = "L_566327653141843049"

# Array of cameras serial numbers
COLLECT_CAMERAS_SERIAL_NUMBERS = ["Q2GV-Y4MD-VSQ6"]
# Array of zone id, all is *. eg ["*"]
COLLECT_ZONE_IDS = ["*"]

# motion trigger setting
MOTION_ALERT_PEOPLE_COUNT_THRESHOLD = 1

MOTION_ALERT_ITERATE_COUNT = 4

MOTION_ALERT_TRIGGER_PEOPLE_COUNT = 0

MOTION_ALERT_PAUSE_TIME = 15

_MONITORING_TRIGGERED = False

_MONITORING_MESSAGE_COUNT = 0

_MONITORING_PEOPLE_TOTAL_COUNT = 0


def collect_zone_information(topic, payload):
    ## /merakimv/Q2GV-S7PZ-FGBK/123

    parameters = topic.split("/")
    serial_number = parameters[2]
    zone_id = parameters[3]
    index = len([i for i, x in enumerate(COLLECT_ZONE_IDS) if x == zone_id])

    # if not wildcard or not in the zone_id list or equal to 0 (whole camera)
    if COLLECT_ZONE_IDS[0] != "*":
        if index == 0 or zone_id == "0":
            return

    # detect motion

    global _MONITORING_TRIGGERED, _MONITORING_MESSAGE_COUNT, _MONITORING_PEOPLE_TOTAL_COUNT

    # if motion monitoring triggered

    if _MONITORING_TRIGGERED:

        _MONITORING_MESSAGE_COUNT = _MONITORING_MESSAGE_COUNT + 1

        _MONITORING_PEOPLE_TOTAL_COUNT = _MONITORING_PEOPLE_TOTAL_COUNT + payload

        if _MONITORING_MESSAGE_COUNT > MOTION_ALERT_ITERATE_COUNT:

            if _MONITORING_PEOPLE_TOTAL_COUNT >= MOTION_ALERT_TRIGGER_PEOPLE_COUNT:
                # notification
                print(serial_number)
                notify(serial_number)
                # pause
                time.sleep(MOTION_ALERT_PAUSE_TIME)

            # reset
            _MONITORING_MESSAGE_COUNT = 0

            _MONITORING_PEOPLE_TOTAL_COUNT = 0

            _MONITORING_TRIGGERED = False

    if payload >= MOTION_ALERT_PEOPLE_COUNT_THRESHOLD:
        _MONITORING_TRIGGERED = True

    print("payload : " + str(payload) +
          ", _MONITORING_TRIGGERED : " + str(_MONITORING_TRIGGERED) +
          ", _MONITORING_MESSAGE_COUNT : " + str(_MONITORING_MESSAGE_COUNT) +
          ", _MONITORING_PEOPLE_TOTAL_COUNT : " + str(_MONITORING_PEOPLE_TOTAL_COUNT))


def notify(serial_number):
    # Get video link
    url = "https://api.meraki.com/api/v0/networks/{1}/cameras/{0}/videoLink".format(serial_number, NETWORK_ID)
    # current timestamp
    ts = str(time.time()).split(".")[0] + "000"

    querystring = {"timestamp": ts}

    headers = {
        'X-Cisco-Meraki-API-Key': MERAKI_API_KEY,
        "Content-Type": "application/json"
    }
    resp = requests.request("GET", url, headers=headers, params=querystring)

    if int(resp.status_code / 100) == 2:
        print("trigger alert")
        msg = "An alert triggered.  \n Video : ".format(resp.json().get("url"))
        sent_notification(msg)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    payload = payload["counts"]["person"]
    parameters = msg.topic.split("/")
    serial_number = parameters[2]

    # filter camera
    '''
    if COLLECT_CAMERAS_SERIAL_NUMBERS[0] != "*" or len(
            [i for i, x in enumerate(COLLECT_CAMERAS_SERIAL_NUMBERS) if x == serial_number]):
        print("why are we returning here?")
        return
    '''

    if msg.topic[-14:] != 'raw_detections':
        collect_zone_information(msg.topic, payload)


if __name__ == "__main__":

    # mqtt
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_SERVER, MQTT_PORT, 60)
        client.loop_forever()
    except Exception as ex:
        print("[MQTT]failed to connect or receive msg from mqtt, due to: \n {0}".format(ex))
