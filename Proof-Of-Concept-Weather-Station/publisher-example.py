import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "127.0.0.1"
client = mqtt.Client("Temperature") 
client.connect(mqttBroker)


while True:
	randomNumber = uniform(20.0, 10.0)
	client.publish("TEMPERATURE", randomNumber) 
	print("Just published " + str(randomNumber) + " to topic \"Temperature\"")
	time.sleep(1)
	


