"""Bai 3 - Smart Light Device: nghe cmd, bao status."""
import json
import os

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"
DEVICE_ID = "light01"

state = {"status": "OFF"}

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def publish_status():
    payload = {"device_id": DEVICE_ID, "status": state["status"]}
    client.publish(TOPIC_STATUS, json.dumps(payload))
    print(f"Trang thai hien tai: {payload}")


def on_connect(c, u, f, rc):
    print(f"Light {DEVICE_ID} online, trang thai={state['status']}")
    c.subscribe(TOPIC_CMD)


def on_message(c, u, msg):
    cmd = msg.payload.decode(errors="replace").strip().upper()
    if cmd in ("ON", "OFF"):
        state["status"] = cmd
        publish_status()
    else:
        print(f"Lenh sai: {cmd!r} (chi nhan ON/OFF)")


client.on_connect = on_connect
client.on_message = on_message


def main():
    client.connect(BROKER, PORT, 60)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()