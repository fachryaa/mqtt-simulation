# python 3.6
from paho.mqtt import client as mqtt_client

from helpers import getCurrentTime, encodePayload, setSpeed, setLatestTag, findNum

def publish(client, topic, payload):
    #train id
    payload['train_id'] = findNum(topic)
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
        print(f"Success {p}")
    else:
        print(f"Failed to send message to topic {topic}")
