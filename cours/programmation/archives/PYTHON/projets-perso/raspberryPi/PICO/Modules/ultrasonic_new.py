import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 37
ECHO = 35
SPEED = 17150
ROUND = 2

print('Distance measurement in progress...')

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

time.sleep(1)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        pulse_start = time.time()
        pulse_end = time.time()

        # Attendre le début du signal d'écho
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Attendre la fin du signal d'écho
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calculer la durée du pulse
        pulse_duration = pulse_end - pulse_start

        # Calculer la distance
        distance = pulse_duration * SPEED
        distance = round(distance, ROUND)

        print('Distance:', distance, 'cm')
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
