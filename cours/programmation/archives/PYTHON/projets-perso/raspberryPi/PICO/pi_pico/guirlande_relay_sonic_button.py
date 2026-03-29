import machine
import time
from machine import Pin

# --- Configuration du capteur ultrasonique ---
TRIG = machine.Pin(17 , machine.Pin.OUT)  # GPIO17 pour le TRIG
ECHO = machine.Pin(18, machine.Pin.IN)   # GPIO18 pour le ECHO

# --- Configuration du relais ---
relais = Pin(16, Pin.OUT)  # GPIO16 pour le relais
relais.value(1)  # Relais désactivé par défaut (1 = OFF)

# --- Configuration du bouton poussoir ---
button = Pin(14, Pin.IN, Pin.PULL_UP)  # GPIO14 pour le bouton (avec pull-up interne)

# --- Fonction pour mesurer la distance avec le capteur ultrasonique ---
def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    
    while not ECHO.value():  # Attendre le début de l'écho
        pass
    start = time.ticks_us()
    
    while ECHO.value():  # Attendre la fin de l'écho
        pass
    end = time.ticks_us()
    
    # Calcul de la distance en cm
    duration = time.ticks_diff(end, start)
    return duration * 340 / 2 / 10000


# --- Boucle principale ---
relais_active = False  # Variable pour suivre l'état du relais
last_button_state = 1  # État précédent du bouton

while True:
    # Lecture de la distance
    dis = distance()
    
    # Lecture de l'état actuel du bouton
    current_button_state = button.value()
    
    # Gestion par le bouton
    if current_button_state == 0 and last_button_state == 1:  # Bouton pressé
        print("Bouton pressé, changement d'état du relais")
        relais_active = not relais_active  # Inverser l'état du relais
        relais.value(0 if relais_active else 1)  # Activer ou désactiver le relais
        print('Distance: %.2f cm' % dis)
        time.sleep(0.3)  # Petit délai pour éviter les rebonds
    
    # Gestion par le capteur ultrasonique
    if not relais_active:  # Si le relais n'est pas encore activé
        if dis < 10:  # Distance inférieure à 10 cm
            print("Distance < 10 cm, activation du relais")
            print('Distance: %.2f cm' % dis)
            relais.value(0)  # Activer le relais (0 = ON)
            relais_active = True  # Marquer le relais comme activé
            time.sleep(1)  # Pause pour éviter des lectures rapides
    
    else:  # Si le relais est déjà activé
        if dis < 10:  # Remettre la main pour désactiver
            print("Distance < 10 cm, désactivation du relais")
            print('Distance: %.2f cm' % dis)
            relais.value(1)  # Désactiver le relais (1 = OFF)
            relais_active = False  # Marquer le relais comme désactivé
            time.sleep(1)  # Pause pour éviter des lectures rapides
    
    # Mettre à jour l'état précédent du bouton
    last_button_state = current_button_state

    # Pause pour éviter des lectures trop rapides
    time.sleep(0.1)
