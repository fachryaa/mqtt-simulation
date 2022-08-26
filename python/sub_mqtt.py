# python 3.6
import random

from paho.mqtt import client as mqtt_client
from connect_mqtt import connect_mqtt
from helpers import decodePayload


def subscribe(client, topic, payload):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        dict = decodePayload(msg.payload.decode())
        payload['is_go'] = dict['is_go']

    client.subscribe(topic)
    client.on_message = on_message
    client.loop_start()
