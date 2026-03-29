#!/usr/bin/python

import RPi.GPIO as GPIO
import time


sound_pin = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:

        if(GPIO.input(sound_pin)==GPIO.LOW):
            print('SOn détecté')
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

# TOUS LES COMMUTATEURS SUR OFF