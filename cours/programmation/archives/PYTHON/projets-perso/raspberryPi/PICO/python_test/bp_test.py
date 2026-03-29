import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(36, GPIO.OUT)

GPIO.setup(40, GPIO.IN)

while True:
    if GPIO.input(40) == (True):
        GPIO.output(36, GPIO.LOW)
        
    else:
        GPIO.output(36, GPIO.HIGH)