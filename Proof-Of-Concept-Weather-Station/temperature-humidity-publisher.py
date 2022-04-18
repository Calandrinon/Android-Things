import RPi.GPIO as GPIO
import dht11
import time
import datetime
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "127.0.0.1"
client = mqtt.Client("Sensor") 
client.connect(mqttBroker)

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=4)

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Temperature: %-3.1f C" % result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)
			client.publish("TEMPERATURE", result.temperature) 
			client.publish("HUMIDITY", result.humidity) 
			print("Just published temperature " + str(result.temperature) + " to topic \"Temperature\"")
			print("Just published humidity " + str(result.humidity) + " to topic \"Humidity\"")
		time.sleep(1)
except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()

