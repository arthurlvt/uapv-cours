from machine import Pin, PWM
import time

# Configuration du servo sur le Pin 12
servo_pin = PWM(Pin(12))
servo_pin.freq(50)  # Fréquence de 50 Hz pour les servos standards

# Configuration du bouton sur le Pin 5 avec une résistance de pull-up
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Fonction pour définir des angles précis
def set_angle(duty):
    servo_pin.duty_u16(duty)

while True:
    if button.value() == 0:  # Si le bouton est appuyé (0 signifie appuyé avec PULL_UP)
        print("You pressed the button!")
        
        # Position à 90°
        set_angle(5500)  # Approximation pour 90°
        time.sleep(0.1)

        # Position à 0°
        set_angle(1638)  # Approximation pour 0°
        time.sleep(0.1)

        # Position à 90°
        set_angle(5500)  # Approximation pour 90°
        time.sleep(2)
