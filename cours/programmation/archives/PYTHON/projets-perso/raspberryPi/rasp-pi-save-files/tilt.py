#!/usr/bin/python

import time
import RPi.GPIO as GPIO

tilt_pin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(tilt_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(tilt_pin):
            print ("[-] Left Tilt")
        else:
            print ("[-] Right Tilt")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()