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
topic = "/dfma/qa"
client_id = "client-001"

# Create IoT simulator to generate random measurements
def IOT_simulator():
    measurement = np.random.uniform(low=20.0, high=30.0)
    return measurement

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

# Publish the measurements obtained from Iot Simulator to /dfma/qa topic
def publish(client):
    i = 0
    while i<5:
        # Interval = 0.05 seconds
        time.sleep(0.05)

        i += 1
        msg = IOT_simulator()
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()