import json

from datetime import datetime

def getCurrentTime():
  now = datetime.now().strftime("%H:%M:%S")
  return(str(now))

def loadJson(path):
  with open(path, 'r') as p:
    return json.load(p)

def encodePayload(payload):
  return '*'.join(map(str,payload.values()))

def decodePayload(str):
  payloadKeys = list(loadJson('payload.json').keys())
  values = str.split('*')

  return dict(zip(payloadKeys, values))


def setSpeed(state, speed):
  if state :
    if speed < 5 : return speed+1
    else : return speed
  else :
    if speed > 0 : return speed-1
    else : return speed


def setLatestTag(speed, loc):
  meter = 0.277778 * speed
  loc += meter
  tag = int(loc/15)

  if tag >= 212 and loc >=3162:
    loc,tag = 0
    return tag, tag
  else :
    return tag, round(loc,2)

  