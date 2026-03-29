import RPi.GPIO as GPIO
import time

# Définissez la broche GPIO que vous avez utilisée pour le capteur de mouvement
MOTION_SENSOR_PIN = 23  # Remplacez par le numéro de la broche GPIO que vous avez utilisée

# Configuration de la broche GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

try:
    print("Attente de détection de mouvement...")
    while True:
        if GPIO.input(MOTION_SENSOR_PIN):
            print("Mouvement détecté!")
            # Ajoutez ici le code que vous souhaitez exécuter lorsque le mouvement est détecté
            time.sleep(2)  # Attendre 2 secondes pour éviter les détections multiples rapprochées
        time.sleep(0.1)  # Attente entre les lectures pour économiser les ressources du CPU

except KeyboardInterrupt:
    pass

finally:
    # Nettoyage des broches GPIO
    GPIO.cleanup()