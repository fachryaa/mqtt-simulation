import time

from paho.mqtt import client as mqtt_client
from connect_mqtt import connect_mqtt
from pub_mqtt import publish
from sub_mqtt import subscribe
from helpers import loadJson

payload = loadJson('./payload.json')

def run(train_id):
  pub_topic = f"{train_id}_info"
  sub_topic = [
    f"{train_id}_go",
    f"{train_id}_seq"
  ]
  client = connect_mqtt()
  while True:
    time.sleep(1)
    publish(client, pub_topic, payload)
    for x in range(len(sub_topic)): subscribe(client, sub_topic[x], payload)