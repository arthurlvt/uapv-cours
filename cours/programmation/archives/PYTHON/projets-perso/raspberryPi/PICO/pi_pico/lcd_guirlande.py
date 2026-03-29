import utime
import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from lcdi2c import I2cLcd
from dht11_api import DHT11, InvalidChecksum

# Configuration de l'I2C et du matériel
led = Pin(16, Pin.OUT)  # LED sur GPIO16
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Broches I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Adresse I2C de l'écran LCD
temperaturepin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(temperaturepin)

# Variables pour suivre l'état
display_temperature = True  # True = afficher la température, False = humidité
switch_interval = 30  # Intervalle entre basculements (secondes)
last_switch_time = utime.time()

led_toggle_interval = 0.5  # Intervalle de clignotement de la LED (secondes)
last_led_toggle_time = utime.time()
led_state = False

while True:
    current_time = utime.time()

    # Lire les données du capteur DHT11
    try:
        temp = sensor.temperature  # Température en °C
        hum = sensor.humidity  # Humidité en %
    except (InvalidChecksum, InvalidPulseCount):
        temp, hum = None, None  # En cas d'erreur de mesure

    # Obtenir la date et l'heure actuelles
    now = utime.localtime()
    date_str = "{:02}/{:02}/{:04}".format(now[2], now[1], now[0])  # Jour/Mois/Année
    time_str = "{:02}:{:02}:{:02}".format(now[3], now[4], now[5])  # Heure:Minute:Seconde

    # Basculer entre température et humidité à intervalles réguliers
    if current_time - last_switch_time >= switch_interval:
        display_temperature = not display_temperature
        last_switch_time = current_time

    # Mettre à jour l'écran LCD
    lcd.clear()
    lcd.putstr("   " + date_str)
    lcd.move_to(0, 1)  # Aller à la deuxième ligne

    if display_temperature:
        lcd.putstr(time_str + " | {}C".format(temp if temp is not None else "Err"))
    else:
        lcd.putstr(time_str + " | {}%".format(hum if hum is not None else "Err"))

    # Clignoter la LED à intervalles réguliers
    if current_time - last_led_toggle_time >= led_toggle_interval:
        led_state = not led_state  # Basculer l'état de la LED
        led.value(led_state)
        last_led_toggle_time = current_time

    # Délai pour éviter une surcharge
    utime.sleep(0.1)
