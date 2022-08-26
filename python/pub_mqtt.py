# python 3.6
from paho.mqtt import client as mqtt_client

from helpers import getCurrentTime, encodePayload, setSpeed, setLatestTag

location = 0

def publish(client, topic, payload):
    msg_count = 0
    global location

    #train id
    payload['train_id'] = 1
    #timestamp
    payload['current_timestamp'] = getCurrentTime()
    #speed
    payload['speed'] = setSpeed(payload['is_go'], payload['speed'])
    #latest tag
    payload['latest_detected_tag'], payload['position']  = setLatestTag(payload['speed'], payload['position'])

    p = encodePayload(payload)

    result = client.publish(topic, p)
    status = result[0]
    if status == 0:
        print('')
    else:
        print(f"Failed to send message to topic {topic}")
    msg_count += 1