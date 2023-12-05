#!/usr/bin/python
import os
import time
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

errorCount = 0
count = 0

while True:
    GPIO.output(37, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(37, GPIO.LOW)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    count = count + 1
    print("Count: " + str(count) + " | Temp: {0:0.1f} C Humidity: {1:0.1f} %".format(temperature, humidity))
    print("Errors: " + str(errorCount))
    if humidity > 70 and humidity < 100:
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)
        os.system('espeak "High humidity detected"')
    elif humidity > 100:
        errorCount = errorCount + 1
        GPIO.output(40, GPIO.HIGH)
        os.system('espeak "Error number"' + str(errorCount))
    else:
        GPIO.output(36, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
    print("--------------------------------------------")
