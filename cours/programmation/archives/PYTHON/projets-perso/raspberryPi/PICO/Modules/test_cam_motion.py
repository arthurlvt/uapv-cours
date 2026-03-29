import RPi.GPIO as GPIO
from picamera import PiCamera
import time

GPIO.setmode(GPIO.BOARD)

PIR_PIN = 7  # Remplacez par le numéro de la broche GPIO que vous avez utilisée pour le capteur de présence

GPIO.setup(PIR_PIN, GPIO.IN)

camera = PiCamera()

try:
    print("Attente de détection de mouvement...")

    while True:
        if GPIO.input(PIR_PIN):
            print("Mouvement détecté! Capture d'image...")
            
            # Capture d'une image avec la caméra
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_filename = f"motion_capture_{timestamp}.jpg"
            camera.capture(image_filename)
            
            print(f"Image capturée : {image_filename}")

            # Attendez un moment pour éviter les détections multiples rapprochées
            time.sleep(5)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()


# NON FONCTIONNEL CAR IMPOSSIBLE AVEC OS
