import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
	print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "127.0.0.1"
client = mqtt.Client("Browser") 
client.connect(mqttBroker)

client.subscribe("TEMPERATURE")
client.subscribe("HUMIDITY")
client.on_message = on_message

client.loop_forever()
