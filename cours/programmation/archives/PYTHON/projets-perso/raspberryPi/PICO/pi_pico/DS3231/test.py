'''
Utilisation d'une horloge temps réel DS3231
avec un Raspberry Pi Pico.
Lecture de la date et de l'heure.
Plus d'infos:
https://electroniqueamateur.blogspot.com/2021/08/horloge-temps-reel-ds3231-et-raspberry.html
'''

import urtc  # https://github.com/adafruit/Adafruit-uRTC
from machine import I2C, Pin
from utime import sleep

i2c = I2C(0,scl=Pin(9), sda=Pin(8))
rtc = urtc.DS3231(i2c)

while True:

    # obtention des infos du DS3231
    maintenant = rtc.datetime()
    
    # affichage sous forme de tuple
    print(maintenant)
    print()

    # affichage plus convivial
    print("Date: {:02d}-{:02d}-{:04d}".format(maintenant.day,maintenant.month,maintenant.year))
    print("Heure: {:02d}:{:02d}:{:02d}".format(maintenant.hour,maintenant.minute,maintenant.second))
    print()
    
    # mise à jour une fois par seconde
    sleep(1)