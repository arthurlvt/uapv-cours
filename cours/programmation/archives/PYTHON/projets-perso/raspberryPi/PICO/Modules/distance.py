#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)

TRIG = 36
ECHO = 32

try:
    num_measurements = int(input('Combien de valeurs significatives voulez-vous ? '))

except ValueError:
    print('Veuillez entrer une valeur numérique ! ')
    sys.exit(1)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("-->...")
time.sleep(2)

distances = []

for _ in range(num_measurements):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    distances.append(distance)

    print("Distance:", distance, "cm")

    time.sleep(1)

average_distance = sum(distances) / len(distances)

print("Distance Moyenne:", round(average_distance, 2), "cm")

GPIO.cleanup()
