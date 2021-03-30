'''
Assignment 2:

a) Write a IoT simulator to publish random measurement between 20.0 to 30.0 using paho publish module at 0.05 sec interval 
in dfma/qa topic channel

b) Specification of the product is 25.0 +/- 3.0. Create a mqtt subscriber in python to listen to above channel and 
send message "reject" in dfma/qa/reject channel whenever measurement falls outside the specification

c) Plot a running bar graph on Nos of item rejected. Update it every min.
'''

import time
import numpy as np
from paho.mqtt import client as mqtt_client

broker = '127.0.0.1'
topic = "/dfma/qa/reject"
client_id = "client-003"

# Connect to mqtt client
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker)
    return client

# Subscribe to dfma/qa topic channel to get IoT simulator readings
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()