import RPi.GPIO as GPIO
import dht11
import time
import datetime
import matplotlib.pyplot as plt

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 4
instance = dht11.DHT11(pin=4)
timestamps, temperature_values, humidity_values = [], [], []

try:
    while True:
        result = instance.read()
        if result.is_valid():
            timestamps.append(datetime.datetime.now())
            temperature_values.append(result.temperature)
            humidity_values.append(result.humidity)
            print("Last valid input: " + str(timestamps[-1]))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            figure, axes = plt.subplots(1, 2, figsize=(10, 8))
            axes[0].plot(timestamps, temperature_values)
            axes[1].plot(timestamps, humidity_values)
            plt.pause(0.05)
            plt.show()
        time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

