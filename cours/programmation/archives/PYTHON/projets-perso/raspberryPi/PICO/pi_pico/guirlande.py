from machine import Pin
import time  # Utilisation de time.sleep pour être cohérent

# Configuration des broches
led = Pin(16, Pin.OUT)  # La LED est sur GPIO16
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Le bouton est sur GPIO14 avec une résistance de pull-up

while True:
    if button.value() == 0:  # Bouton pressé (valeur basse en raison de la pull-up)
        led.value(1)  # Allume la LED
        time.sleep(0.1)  # Pause de 0,5 seconde
        led.value(0)  # Éteint la LED
    else:
        led.value(0)  # Assure que la LED reste éteinte quand le bouton n'est pas pressé
