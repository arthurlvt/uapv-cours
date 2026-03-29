import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

# Définissez l'adresse I2C de l'écran LCD
LCD_I2C_ADDR = 0x21

# Initialisez l'écran LCD avec l'adresse I2C
lcd = CharLCD(i2c_expander='PCF8574', address=LCD_I2C_ADDR, port=1, cols=16, rows=2)

try:
    # Écrire "Hello World" sur l'écran LCD
    lcd.write_string("Hello World")

    # Attendre pendant quelques secondes
    input("Appuyez sur Enter pour quitter...")

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    # Nettoyer les ressources GPIO
    GPIO.cleanup()
