import time
import datetime as dt
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Définir le nombre de lignes et de colonnes du LCD
lcd_columns = 16
lcd_rows = 2

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

lcd.backlight = True
lcd.message ='hello\nsalut'

