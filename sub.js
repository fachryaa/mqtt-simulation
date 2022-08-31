const mqtt = require('mqtt');
const { splitToJson } = require('./helpers/split-to-json');

require('dotenv').config();

const topic = 'train_1_info'

const clientId = process.env.MQTT_CLIENT_ID;
const connectUrl = `mqtt://${process.env.MQTT_HOST}:${process.env.MQTT_PORT}`
const client = mqtt.connect(connectUrl, {
  clientId,
  clean: process.env.MQTT_CLEAN,
  connectTimeout: process.env.MQTT_CONNECT_TIMEOUT,
  username: process.env.MQTT_USERNAME,
  password: process.env.MQTT_PASSWORD,
  reconnectPeriod: process.env.MQTT_RECONNECT_PERIOD,
})

client.on('connect', () => {
  console.log('Connected')
  client.subscribe([topic], () => {
    console.log(`Subscribe to topic '${topic}'`)
  })
})

client.on('message', (topic, payload) => {
  const msg = splitToJson(payload)
  console.log(topic, msg)
})
