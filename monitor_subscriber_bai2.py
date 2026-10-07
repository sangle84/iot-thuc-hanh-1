"""Bai 2 - Monitoring Subscriber: doc JSON + canh bao nguong."""
import json
import os

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def on_connect(c, u, f, rc):
    print(f"Da ket noi, rc={rc}. Dang nghe {TOPIC} (Ctrl+C de dung)...")
    c.subscribe(TOPIC)


def on_message(c, u, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"Device: {data.get('device_id')}")
        print(f"Temperature: {data.get('temperature')} C")
        print(f"Humidity: {data.get('humidity')} %")
        if data.get("temperature", 0) > 35:
            print("CANH BAO: Nhiet do cao")
        if data.get("humidity", 100) < 40:
            print("CANH BAO: Do am thap")
    except (json.JSONDecodeError, UnicodeDecodeError):
        print(f"Payload loi: {msg.payload!r}")


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