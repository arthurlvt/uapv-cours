from RPLCD.i2c import CharLCD
import machine
import time
import datetime as dt
import Adafruit_DHT

# Configuration du capteur DHT11
sensor = Adafruit_DHT.DHT11
DHTpin = 19  # Changez si nécessaire
led_pin = 6  # Changez si nécessaire

# Configuration de GPIO
led = machine.Pin(led_pin, machine.Pin.OUT)  # Initialisation de la LED

# Configuration de l'écran LCD
i2c_addr = 0x27  # Adresse I2C de l'écran LCD
lcd = CharLCD('PCF8574', i2c_addr, rows=2, cols=16)  # Initialisation de l'écran LCD

lcd.backlight = True  # Allumer le rétroéclairage de l'écran

try:
    while True:
        # Lecture de l'humidité et de la température
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHTpin)
        
        # Vérifiez si les données sont valides
        if humidity is not None and temperature is not None:
            now = dt.datetime.now()
            
            # Affichage de la date et de l'heure sur l'écran LCD
            lcd.write_string('   ' + now.strftime('%d/%m/%Y'))
            lcd.cursor_pos = (1, 0)  # Positionner le curseur à la deuxième ligne
            lcd.write_string(now.strftime('%X') + ' | ' + str(temperature) + 'C')
            
            # Vérification de la température
            if temperature <= 18:
                print('TEMPERATURE UNDER 18 DEGRES!!')
                for x in range(10):
                    led.on()  # Allumer la LED
                    time.sleep(0.1)
                    led.off()  # Éteindre la LED
                    time.sleep(0.1)
            else:
                led.off()  # Éteindre la LED
            
            time.sleep(1)  # Pause d'une seconde
            lcd.clear()  # Effacer l'affichage LCD
        else:
            print('Failed to retrieve data from humidity sensor')
            time.sleep(2)  # Attendre avant de réessayer
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False  # Éteindre le rétroéclairage de l'écran
