import sys
import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

vibration_pin = 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(vibration_pin, GPIO.OUT)

try:
    for i in range(1):
        print("Présentez votre badge RFID...")
        print()

        # Ajout de l'étape d'authentification explicite
        authenticated = False
        while not authenticated:
            try:
                id, text = reader.read()
                authenticated = True
            except Exception as e:
                print(f"Erreur d'authentification : {e}")
                time.sleep(1)

        if text.strip():  # Vérifie si le contenu n'est pas une chaîne vide
            print(f"Identifiant du badge : {id}")
            print()

            # Ajoutez une condition pour vérifier l'identifiant spécifique
            if id == 862062525869:
                name = "Arthur"
                print("Bienvenue", name, "!")
                GPIO.output(vibration_pin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(vibration_pin, GPIO.LOW)
            else:
                print(f"Numéro d'identifiant : {id}, Contenu : {text}")
        else:
            print("Votre badge est vide ou invalide. Arrêt du programme.")
            sys.exit(0)
except KeyboardInterrupt:
    print("Arrêt du programme.")
finally:
    GPIO.cleanup()
    
# POUR FAIRE FONCTIONNER LE VIBRATOR, METTRE COMMUTATEURS EN OFF SAUF 1 DU BLOC DROIT
