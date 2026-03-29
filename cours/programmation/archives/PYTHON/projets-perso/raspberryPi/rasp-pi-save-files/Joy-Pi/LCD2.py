import time
import datetime as dt
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import Adafruit_DHT

# Définir le nombre de lignes et de colonnes du LCD
lcd_columns = 16
lcd_rows = 2
sensor = Adafruit_DHT.DHT11
dht_pin = 4

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

lcd.backlight = True

# Variables pour mémoriser les valeurs précédentes
previous_temp = None
previous_humidity = None
previous_time = ""

try:
    while True:
        # Lire la température et l'humidité
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        
        # Obtenir l'heure actuelle
        now = dt.datetime.now()
        current_time = now.strftime('%X')  # Heure sous format HH:MM:SS
        current_date = now.strftime('%x')  # Date sous format MM/DD/YY

        # Mettre à jour l'heure seulement si elle a changé
        if current_time != previous_time:
            lcd.cursor_position(0, 0)  # Positionner le curseur à la ligne 1
            lcd.message = current_date + '\n' + current_time  # Afficher date et heure
            previous_time = current_time  # Mémoriser la nouvelle heure
        
        # Mettre à jour la température et l'humidité si elles ont changé
        if humidity is not None and temperature is not None:
            if temperature != previous_temp:
                lcd.cursor_position(12, 1)  # Positionner le curseur à droite de l'heure
                lcd.message = f"{temperature}C"  # Afficher la température
                previous_temp = temperature  # Mémoriser la nouvelle température

        time.sleep(1)  # Attendre 1 seconde avant la prochaine mise à jour
    
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
