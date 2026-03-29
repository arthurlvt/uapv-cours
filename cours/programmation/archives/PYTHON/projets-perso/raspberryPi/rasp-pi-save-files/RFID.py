import sys
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Présentez votre badge RFID...")
    while True:
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
            print(f"Contenu du badge : {text}")

            # Ajoutez une condition pour vérifier l'identifiant spécifique
            if id == 862062525869:
                print("Bienvenue!")
            else:
                print(f"Numéro d'identifiant : {id}, Contenu : {text}")
        else:
            print("Votre badge est vide. Arrêt du programme.")
            sys.exit(0)
except KeyboardInterrupt:
    print("Arrêt du programme.")
finally:
    GPIO.cleanup()
