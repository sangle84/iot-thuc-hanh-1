"""Bai 3 - Controller App: nhap ON/OFF, gui cmd, hien status."""
import os

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.emqx.io")
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    client = mqtt.Client()  # paho-mqtt < 2.0


def on_connect(c, u, f, rc):
    print(f"Da ket noi, rc={rc}.")
    c.subscribe(TOPIC_STATUS)
    print("Nhap lenh: ON / OFF (EXIT de thoat)")


def on_message(c, u, msg):
    print(f"\nTrang thai nhan duoc:\n{msg.payload.decode(errors='replace')}")


client.on_connect = on_connect
client.on_message = on_message


def main():
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    try:
        while True:
            cmd = input("Nhap lenh: ").strip().upper()
            if cmd == "EXIT":
                break
            if cmd not in ("ON", "OFF"):
                print("Loi: chi nhap ON, OFF hoac EXIT")
                continue
            client.publish(TOPIC_CMD, cmd)
            print(f"Da gui lenh {cmd} toi light01")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()