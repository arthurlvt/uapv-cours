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
humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)

lcd.backlight = True

try:
    while True:
        now = dt.datetime.now()
        lcd.message ='    ' + now.strftime('%x') + '\n' + '' + now.strftime('%X') + ' | ' + str(temperature) + 'C'
    
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
    
# install blinka + 