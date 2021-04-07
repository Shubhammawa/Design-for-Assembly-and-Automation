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
import matplotlib.pyplot as plt
import matplotlib.animation

broker = '127.0.0.1'
topic = "/dfma/qa"
client_id = "client-002"



def quality_check(val):
    '''
    Function quality_check

    Input:
        val --> (float): Reading obtained from mqtt subscriber listening to dfma/qa topic for the IoT simulator reading

    Output:
        "reject" --> (string): Sends message reject whenever val is outside specification limits
    '''

    # Limits: 25.0 +/- 3.0
    lcl = 22.0
    ucl = 28.0

    if(val<lcl or val>ucl):
        quality_check.num_rejects += 1
        print(quality_check.num_rejects)
        # plt.bar(time.time(),quality_check.num_rejects)
        # plt.show(block=False)
        # plt.pause(3)
        # plt.close('all')
        return 1
    else:
        return 0

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
        
        measurement = float(msg.payload.decode())
        reject = quality_check(measurement)

        
        if(reject == 1):
        #result = client.publish(topic, msg)
            msg = 'reject'
            topic_2 = '/dfma/qa/reject'
            client.publish(topic_2, msg)
            print(f"Send `{msg}` to topic `{topic_2}`")
    client.subscribe(topic)
    client.on_message = on_message
    


def run():
    quality_check.num_rejects = 0
    client = connect_mqtt()
    subscribe(client)
    #publish(client)
    client.loop_forever()
    


if __name__ == '__main__':
    run()