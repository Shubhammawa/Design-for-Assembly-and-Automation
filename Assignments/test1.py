import time
import paho.mqtt.client as mqtt_client

broker = "127.0.0.1"
topic = "/dfma/test"
client_id = "client-001"

# Define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("Received message = ", str(message.payload.decode("utf-8")))

# Create client
client = mqtt_client.Client(client_id)
client.on_message = on_message
print("Connecting to broker ", broker)

# Connect
client.connect(broker)

# Start loop to process received messages
client.loop_start()
print("Subscribing")

client.subscribe("dfma/test/#")
time.sleep(2)

while True:
    client.on_message