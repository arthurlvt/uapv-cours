import utime
import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from dht11_api import DHT11, InvalidChecksum, InvalidPulseCount


# Configuration de l'I2C
led = Pin(16, Pin.OUT)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Remplacez les broches si nécessaire
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Adresse I2C de l'écran LCD
temperaturepin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(temperaturepin)

# Variable pour suivre l'affichage actuel (True = température, False = humidité)
display_temperature = True

# Délai entre les basculements (en secondes)
switch_interval = 30
last_switch_time = utime.time()

while True:
    try:
        #  Lire les données du capteur DHT11
        temp = sensor.temperature  # Température en °C
        hum = sensor.humidity  # Humidité en %
    except (InvalidChecksum, InvalidPulseCount):
        temp, hum = None, None  # En cas d'erreur de mesure

    # Récupérer l'heure actuelle
    now = utime.localtime()
    date_str = "{:02}/{:02}/{:04}".format(now[2], now[1], now[0])  # Jour/Mois/Année
    time_str = "{:02}:{:02}:{:02}".format(now[3], now[4], now[5])  # Heure:Minute:Seconde

    # Effacer l'écran LCD
    lcd.clear()
    lcd.putstr("   " + date_str)
    lcd.move_to(0, 1)  # Aller à la deuxième ligne

    # Basculer entre température et humidité
    if display_temperature:
        lcd.putstr(time_str + " | {}C".format(temp if temp is not None else "Err"))
    else:
        lcd.putstr(time_str + " | {}%".format(hum if hum is not None else "Err"))

    # Vérifier si l'intervalle est écoulé pour changer l'affichage
    current_time = utime.time()
    if current_time - last_switch_time >= switch_interval:
        display_temperature = not display_temperature  # Basculer entre température et humidité
        last_switch_time = current_time  # Réinitialiser le temps du dernier basculement

    # Délai avant la prochaine mise à jour
    utime.sleep(1)
    
    
