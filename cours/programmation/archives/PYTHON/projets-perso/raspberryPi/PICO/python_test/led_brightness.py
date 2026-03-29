import RPi.GPIO as GPIO
import time

# Définir la broche de la LED
LED = 33  # Broche physique 33 (GPIO 13)

# Initialisation des broches
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)  # Configurer Led1 comme sortie
GPIO.setwarnings(False)

# Initialiser le PWM sur la broche Led1 avec une fréquence de 1000 Hz
pwm_led = GPIO.PWM(LED, 1000)
pwm_led.start(0)  # Démarrer le PWM avec une intensité de 0% (LED éteinte)

try:
    # Augmenter progressivement l'intensité de la LED
    for duty_cycle in range(100, -1, -1):  # De 0% à 100% par pas de 1%
        pwm_led.ChangeDutyCycle(duty_cycle)
        duty_cycle = duty_cycle/2
        duty_cycle = 50 - duty_cycle
        print(f"Intensité LED : {duty_cycle * 2}%")
        time.sleep(0.1)

    # Fixer l'intensité de la LED à 50%
    pwm_led.ChangeDutyCycle(20)
    print("Intensité LED fixée à 20%.")

    while True:
        time.sleep(5)  # Maintenir 50% pendant 5 secondes

except KeyboardInterrupt:
    print('Rebooting...')
    pwm_led.stop()
    GPIO.cleanup()
