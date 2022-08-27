from paho.mqtt import client as mqtt_client
import random
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
broker = CONFIG['MQTT_HOST']
port = int(CONFIG['MQTT_PORT'])
username = CONFIG['MQTT_USERNAME']
password = CONFIG['MQTT_PASSWORD']

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client