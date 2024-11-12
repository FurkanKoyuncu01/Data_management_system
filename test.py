import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker Bilgileri
MQTT_BROKER = "192.168.103.110"  # Broker adresini buraya yazın
MQTT_PORT = 1883
MQTT_USERNAME = "agv"
MQTT_PASSWORD = "123"
MQTT_TOPIC = "robot1/amcl_pose"  # Test etmek istediğiniz topic

def connect_mqtt():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT)
    print(f"Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
    return client

def publish_messages(client):
    try:
        while True:
            # Örnek JSON mesajı
            message = {
                "pose": {
                    "pose": {
                        "position": {"x": 1.0, "y": 2.0},
                        "orientation": {"w": 0.5}
                    }
                }
            }
            # Mesajı JSON formatında yayınla
            client.publish(MQTT_TOPIC, json.dumps(message))
            print(f"Published to {MQTT_TOPIC}: {message}")

            # 2 saniyede bir mesaj gönder
            time.sleep(2)
    except KeyboardInterrupt:
        print("Message publishing stopped.")

if __name__ == "__main__":
    mqtt_client = connect_mqtt()
    publish_messages(mqtt_client)
