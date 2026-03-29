from RPLCD.i2c import CharLCD
import machine
import time
import datetime as dt

# Adresse I2C de l'écran LCD
i2c_addr = 0x27
lcd = CharLCD('PCF8574', i2c_addr, rows=2, cols=16)

lcd.backlight = True  # Allumer le rétroéclairage de l'écran

try:
    while True:
        now = dt.datetime.now()
        lcd.write_string('    ' + now.strftime('%d/%m/%Y'))
        lcd.cursor_pos = (1, 0)  # Positionner le curseur à la deuxième ligne
        lcd.write_string(now.strftime('%X') + ' | ')
        time.sleep(1)
        lcd.clear()  # Effacer l'affichage LCD
except KeyboardInterrupt:
    lcd.clear()  # Effacer l'affichage à l'arrêt du programme
    lcd.backlight = False  # Éteindre le rétroéclairage de l'écran
