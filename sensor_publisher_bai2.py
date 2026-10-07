"""Bai 2 - Sensor Publisher: gui JSON nhiet do / do am moi 3s."""
import json
import os
import random
import time

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC = "iot/lab/sensor01/data"
DEVICE_ID = "sensor01"

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def main():
    client.connect(BROKER, PORT, 60)
    print(f"Sensor {DEVICE_ID} dang gui moi 3s (Ctrl+C de dung)...")
    try:
        while True:
            payload = {
                "device_id": DEVICE_ID,
                "temperature": round(random.uniform(20.0, 40.0), 1),
                "humidity": round(random.uniform(30.0, 90.0), 1),
            }
            client.publish(TOPIC, json.dumps(payload))
            print(f"Da gui: {payload}")
            time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()