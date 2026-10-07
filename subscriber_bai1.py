"""Bai 1 - Subscriber: nghe iot/lab/message."""
from datetime import datetime
import os

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC = "iot/lab/message"

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def on_connect(c, u, f, rc):
    print(f"Da ket noi, rc={rc}. Dang nghe {TOPIC} (Ctrl+C de dung)...")
    c.subscribe(TOPIC)


def on_message(c, u, msg):
    print("Nhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode(errors='replace')}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")


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
