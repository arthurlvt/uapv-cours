#!/usr/bin/python
import RPi.GPIO as GPIO
import time

while True :

  GPIO.setmode(GPIO.BOARD) 

  TRIG = 36 
  ECHO = 32
  led_pin = 37

  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
  GPIO.setup(led_pin, GPIO.OUT)

  f = GPIO.PWM(led_pin, 50) #50Hz

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0: #début de la mesure, capteur ultrasons

    pulse_start = time.time()

  while GPIO.input(ECHO)==1: #fin de la mesure, capteur ultrasons

    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150 #valeur constructeur

  if distance <= 99:

    rp = 99-distance

  else:

    rp =1

  f.start(rp)
  f.ChangeDutyCycle(rp) #On fait varier le rapport cyclique pour changer l’intensité lumineuse
  time.sleep(0.02) #50Hz

  GPIO.cleanup()
