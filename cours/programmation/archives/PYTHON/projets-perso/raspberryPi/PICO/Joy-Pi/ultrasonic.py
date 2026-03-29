import RPi.GPIO as GPIO
import time

# Configuration des broches
TRIG = 37  # Broche GPIO pour le Trig (broche 16)
ECHO = 35  # Broche GPIO pour l'Echo (broche 18)

# Initialisation des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # S'assurer que le Trig est bas
    GPIO.output(TRIG, False)
    time.sleep(2)  # Pause de 2 secondes pour stabiliser le capteur

    # Envoyer un signal sur la broche Trig
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # Garder le signal haut pendant 10 µs
    GPIO.output(TRIG, False)

    # Calculer le temps de réponse (aller-retour)
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculer la durée du signal
    signal_duration = end_time - start_time

    # Calculer la distance en fonction de la vitesse du son (34300 cm/s)
    distance = signal_duration * 17150
    distance = round(distance, 2)  # Arrondir à 2 décimales

    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance mesurée : {distance} cm")
        time.sleep(1)  # Pause d'1 seconde avant la prochaine mesure

except KeyboardInterrupt:
    print("Programme interrompu")
    GPIO.cleanup()  # Réinitialiser les broches GPIO
