import paho.mqtt.publish as publish
import paho.mqtt.client as paho

broker = "127.0.0.1"
client = paho.Client("client-001")
client.connect(broker)

client.loop_start()

client.subscribe("dfma/test/#")

publish.single(topic="dfma/test", payload="payload", hostname="127.0.0.1", client_id="client-001")