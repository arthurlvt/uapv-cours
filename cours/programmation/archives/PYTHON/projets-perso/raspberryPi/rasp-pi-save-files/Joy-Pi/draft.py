import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

MOTION_SENSOR_PIN_BCM = 23
VIBRATION_PIN_BOARD = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTION_SENSOR_PIN_BCM, GPIO.IN)
GPIO.setup(VIBRATION_PIN_BOARD, GPIO.OUT)

try:
    print('Checking in process...')

    while True:
        if GPIO.input(MOTION_SENSOR_PIN_BCM):
            print('A motion has just been detected !')
            GPIO.output(VIBRATION_PIN_BOARD, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(VIBRATION_PIN_BOARD, GPIO.HIGH)
            time.sleep(0.5)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
