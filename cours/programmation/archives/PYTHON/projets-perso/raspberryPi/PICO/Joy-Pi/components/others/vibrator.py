# THIS PROGRAM ALLOWS TO KNOW HOW TO USE A VIBRATOR

import RPi.GPIO as GPIO # Importing this library to use GIPO pins
import time # Importing time
import warnings # Importing warnings to remove useless warnings
warnings.filterwarnings("ignore")

vibration_pin = 13 # The vibrator sensor is connected by the pin 13

GPIO.setmode(13, GPIO.BOARD) # The 13td pin is defined as BOARD MODE
GPIO.setup(vibration_pin, GPIO.OUT) # The vibrator is defined as Output Sensor

try:
  while True:
    GPIO.output(vibration_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(vibration_pin, GPIO.LOW)
    time.sleep(0.5)

except KeyboardInterrupt:
  GPIO.cleanup()