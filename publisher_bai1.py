"""Bai 1 - Publisher: gui thong diep len iot/lab/message."""
import os

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC = "iot/lab/message"

HO_TEN = ""
MA_SV = ""

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def main():
    global HO_TEN, MA_SV
    if not HO_TEN:
        HO_TEN = input("Nhap ho ten: ").strip()
    if not MA_SV:
        MA_SV = input("Nhap ma SV: ").strip()
    client.connect(BROKER, PORT, 60)
    print(f"Da ket noi {BROKER}:{PORT}")
    print("Nhap tin nhan (EXIT de thoat):")
    while True:
        try:
            msg = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if msg.upper() in ("EXIT", "QUIT"):
            break
        if not msg:
            continue
        payload = f"{msg} - {MA_SV} - {HO_TEN}"
        client.publish(TOPIC, payload)
        print(f"Da gui -> {TOPIC}: {payload}")
    client.disconnect()


if __name__ == "__main__":
    main()