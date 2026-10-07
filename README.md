# Buổi thực hành 1 - MQTT

## 0. Thông Tin Sinh Viên
| Họ và Tên | Mã Sinh Viên |
| :--- | :--- |
| **Nguyễn Quốc Thịnh** | `B23DCCN790` |
| **Lê Tiến Sang** | `B23DCCN710` |

## 1. Broker
- `broker.emqx.io:1883`, không auth.
- Đổi broker: `MQTT_BROKER=test.mosquitto.org`.
- Cài lib: `pip install paho-mqtt`

## 2. Cách chạy
```text
# Bài 1
python subscriber_bai1.py   # terminal 1
python publisher_bai1.py    # terminal 2

# Bài 2
python monitor_subscriber_bai2.py  # terminal 1
python sensor_publisher_bai2.py    # terminal 2

# Bài 3
python device_bai3.py      # terminal 1
python controller_bai3.py  # terminal 2
```

## 3. Kết quả đạt được
Bài 1 - Publisher:
```text
Nhap ho ten: Nguyen Van A
Nhap ma SV: B23DCCN001
Da ket noi broker.emqx.io:1883
> Xin chao tu client Python MQTT
Da gui -> iot/lab/message: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
```

Bài 1 - Subscriber:
```text
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
Time: 10:15:20
```

Bài 2 - Monitor:
```text
Device: sensor01
Temperature: 36.1 C
Humidity: 38.7 %
CANH BAO: Nhiet do cao
CANH BAO: Do am thap
```

Bài 3 - Controller:
```text
Nhap lenh: ON
Da gui lenh ON toi light01
Trang thai nhan duoc:
{"device_id": "light01", "status": "ON"}
```
