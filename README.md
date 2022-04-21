# Android-Things
Lectures and labs for the IoT course (also called Android-Things, like the old platform deprecated by Google)  

## Resources
- [NeuralPi - RaspberryPi guitar pedal using an LSTM model](https://github.com/GuitarML/NeuralPi)
- [Arduino FM Radio](https://www.youtube.com/watch?v=n1hPj2wfsnA)
- [A simple audio amplifier](https://duino4projects.com/simple-audio-amplifier/)
- [RaspberryPi + Arduino Serial Communication](https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/)
- [DHT11 sensor setup on Raspberry Pi](https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
- [DHT11 Python library](https://github.com/szazo/DHT11_Python)
- [MQTT and sensors](https://www.inzata.com/making-sense-of-iot-sensors-mqtt-and-streaming-data/)

## Ideas

- Puredata-powered guitar pedal with Raspberry Pi, controlled by a simple Android app

	The goal of this project is to create a guitar pedal from a Raspberry Pi, a device which processes the analog signal coming from the guitar and applies an effect on it e.g distortion, fuzz, overdrive, tremolo, echo). The effect produced by the pedal can be controlled by a simple Android app with buttons and knobs.
	To create the sound effect, we can use the visual programming language Puredata.
	In order to connect the guitar to the pedal and the pedal to the amp, we can use a sound card/DAC/ADC such as [Hifiberry DAC+ADC](https://ro.farnell.com/hifiberry/4260439550583/dac-adc-hi-res-dac-adc-for-rpi/dp/3404429)


- Weather monitoring system

	This project collects temperature, humidity and barometric data which is uploaded to a cloud service (probably Heroku) and displayed on a webpage with graphs containing the values for the variation of these quantities over time.

	The components needed are:

		- [Temperature and humidity sensor DHT11](https://www.emag.ro/senzor-de-temperatura-si-umiditate-dht11-arduino-ai051-s37/pd/D9CZ56BBM/)

		- [Temperature and pressure sensor BMP180](https://www.emag.ro/modul-senzor-de-temperatura-si-presiune-bmp180-arduino-ai027-s35/pd/DGTW95BBM/?cmpid=87002&gclid=CjwKCAjwoduRBhA4EiwACL5RP2V_N2unriYwi9VyThR9jbFz25nsvyxYC1U8lIe3E_DeiDsGHe0BqxoCF0EQAvD_BwE)

		- A Raspberry Pi 

			or

		- An Arduino with a WiFi module


## Setup

![Setup](IMG_20220414_155744.jpg)

## Diagram

The setup contains a single DHT11 sensor which is supposed to obtain the temperature and the humidity of the environment. The VCC pin of the sensor is the power supply pin which is connected to the pin no. 2 on the board. The signal pin is used to obtain the temperature and humidity, while the ground pin of the sensor is connected to the 6th pin (ground) on the board. The third pin of the sensor is unused. In order to limit current, a 4.7K Ohm resistor is placed between the VCC and the signal pin.

![Diagram](rpi-dht11.png)

For the Python scripts used to read and stream the sensor data, the RPI.GPIO module is responsible for obtaining the sensor values, while the paho.mqtt module sends/receives messages containing the sensor values to/from a Mosquitto MQTT broker installed locally on the Raspberry Pi (hence the 127.0.0.1 IP for the broker address in the script). 

A next step would be to create a small Angular project and a plot with Plotly which would display the values visually. To subscribe to the stream of data coming from the Python script through the broker, one could use Observables. 

