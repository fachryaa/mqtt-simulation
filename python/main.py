import time

from paho.mqtt import client as mqtt_client
from connect_mqtt import connect_mqtt
from pub_mqtt import publish
from sub_mqtt import subscribe
from helpers import loadJson

payload = loadJson('./payload.json')
topic = 'train_1_info'

def run():
  client = connect_mqtt()
  #client.loop_start()
  while True:
    time.sleep(1)
    publish(client, topic, payload)
    subscribe(client, topic, payload)

if __name__ == '__main__':
    run()