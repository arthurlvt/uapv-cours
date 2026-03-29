from machine import Pin
from time import sleep, ticks_us, ticks_diff
import neopixel

# Configurez le capteur IR
ir_pin = Pin(15, Pin.IN)  # Utilisez GP15 pour l'entrée du capteur IR

# Configurez la barre de LEDs WS2812B sur GPIO16
led_pin = Pin(16, Pin.OUT)  # Utilisez GP16 pour contrôler les LEDs
num_leds = 8
np = neopixel.NeoPixel(led_pin, num_leds)

# Fonction pour lire les signaux IR
def read_ir_signal():
    pulse_times = []
    while ir_pin.value() == 1:
        pass  # Attendre le début du signal
    start_time = ticks_us()
    while len(pulse_times) < 100:  # Limitez le nombre de pulses capturés
        while ir_pin.value() == 0:
            pass
        pulse_start = ticks_us()
        while ir_pin.value() == 1:
            pass
        pulse_end = ticks_us()
        pulse_times.append(ticks_diff(pulse_end, pulse_start))
    return pulse_times

# Fonction pour allumer les LEDs avec des couleurs différentes
def turn_on_leds_with_colors():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
              (0, 255, 255), (255, 0, 255), (128, 128, 128), (255, 255, 255)]
    for i in range(num_leds):
        np[i] = colors[i]  # Assigne une couleur différente à chaque LED
    np.write()

# Fonction pour éteindre toutes les LEDs
def turn_off_leds():
    for i in range(num_leds):
        np[i] = (0, 0, 0)
    np.write()

while True:
    print("Appuyez sur un bouton de la télécommande...")
    pulses = read_ir_signal()
    
    # Si des pulses sont reçus, allumer les LEDs avec des couleurs différentes
    if pulses:
        print("Signal détecté ! Les LEDs s'allument.")
        turn_on_leds_with_colors()
    else:
        turn_off_leds()
    
    # Délai avant la prochaine vérification
    sleep(1)
    turn_off_leds()  # Éteindre les LEDs après 1 seconde
