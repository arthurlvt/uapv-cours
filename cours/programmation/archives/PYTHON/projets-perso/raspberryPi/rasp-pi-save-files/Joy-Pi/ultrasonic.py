import RPi.GPIO as GPIO
import time

# Définir les broches GPIO pour le capteur
TRIG_PIN = 17
ECHO_PIN = 18

# Configuration des broches GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Émission d'une impulsion ultrasonique
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    # Enregistrement du temps d'émission
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    # Enregistrement du temps de réception
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    # Calcul de la distance
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # La vitesse du son est d'environ 343 m/s

    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
# COMMUTATEURS TOUS SUR OFF
