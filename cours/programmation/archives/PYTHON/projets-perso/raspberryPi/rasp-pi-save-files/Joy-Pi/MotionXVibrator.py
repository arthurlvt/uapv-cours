# RFID (Radio Frequency Identification) is a tag reader (all types of tags)
# Motion is literally a motion detector
# This program is a projects made with motion sensor and vibrator
# To make this program, you'll need only 2 frameworks such as GPIO, and time that you have to install in your raspberry

import RPi.GPIO as GPIO
import sys as sys
import time as time
from mfrc522 import SimpleMFRC522

SimpleMFRC522 = 'MFRC'

MOTION_SENSOR_PIN = 23
VIBRATION_PIN = 13

GPIO.setmode(MOTION_SENSOR_PIN, GPIO.BCM)
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

GPIO.setmode(VIBRATION_PIN, GPIO.BOARD)
GPIO.setup(VIBRATION_PIN, GPIO.OUT)d

try:
    print('Checking in process...')

    while True:
        if GPIO.input(MOTION_SENSOR_PIN):
            print('A motion has just been detected !')
            GPIO.output(VIBRATION_PIN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(VIBRATION_PIN, GPIO.HIGH)
            time.sleep(0.5)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

# You can press CTRL + C to stop the program
