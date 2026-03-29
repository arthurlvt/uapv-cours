from machine import Pin
from time import sleep, ticks_us, ticks_diff

# Configurez le capteur IR
ir_pin = Pin(15, Pin.IN)  # Utilisez GP15 pour l'entrée du capteur IR

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

while True:
    print("Appuyez sur un bouton de la télécommande...")
    pulses = read_ir_signal()
    print("Pulses reçus : ", pulses)
    sleep(1)
