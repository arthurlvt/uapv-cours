# YOU NEED TO INSTALL 2 MORE LIBRARIES : adafruit-circuitpython-charlcd and Blinkaio !
# TO INSTALL BLINKA, YOU SHOULD FOLLOW THIS PAGE: https://gallaugher.com/makersnack-installing-circuitpython-on-a-raspberry-pi/
# TO MAKE THIS COMPONENT FUNCTIONAL, PUT OFF ALL SWITCHES

import time # Importing time
import datetime as dt # Importing datetime
import board # It's installed with Blinka
import busio # It's installed with Blinka
import adafruit_character_lcd.character_lcd_i2c as character_lcd # This library allows to do a lot of thinks with sensors and components

# Number of columns in the LCD screen
lcd_columns = '16' # Don't try to change it, it won't change
# Number of rows in the LCD screen
lcd_rows = '2' # Don't try to change it, it won't change

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x27)

lcd.backlight = True # Screen Display ON

try:
  while True:
    lcd.message = 'Hello World!' # I made a project with LCD

except KeyboardInterrupt:
  lcd.clear() # REMOVE ALL ELEMENT ON THE SCREEN
  lcd.backlight = False # Screen Display OFF 