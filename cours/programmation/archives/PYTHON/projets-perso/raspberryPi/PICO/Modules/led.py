import RPi.GPIO as GPIO
import time

LED_PIN = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setwarnings(False)

for x in range(0, 10):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()
