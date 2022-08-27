# python 3.6
import random

from paho.mqtt import client as mqtt_client
from helpers import toJson, getKey


def subscribe(client, topic, payload):
    def on_message(client, userdata, msg):
        msgJson = toJson(msg.payload.decode())
        key = getKey(msgJson)

        payload[key] = msgJson[key]

    client.subscribe(topic)
    client.on_message = on_message
    client.loop_start()

