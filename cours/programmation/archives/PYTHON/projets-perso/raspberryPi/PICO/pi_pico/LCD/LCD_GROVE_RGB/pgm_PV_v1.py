from machine import I2C, Pin, ADC
import utime

# Grove LCD RGB Backlight I2C
LCD_ADDRESS = 0x3e  # Essaie aussi 0x3f si cela ne fonctionne pas
RGB_ADDRESS = 0x30

i2c = I2C(0, scl=Pin(1), sda=Pin(0))

def lcd_write(cmd, mode=0):
    i2c.writeto_mem(LCD_ADDRESS, mode, bytes([cmd]))

def lcd_set_text(text):
    lcd_write(0x01)  # Clear the display
    utime.sleep_ms(2)  # Wait for clear to finish
    lcd_write(0x08 | 0x04)  # Display on
    lcd_write(0x28)  # 2 lines
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            lcd_write(0xc0)  # next line
            if c == '\n':
                continue
        count += 1
        i2c.writeto_mem(LCD_ADDRESS, 0x40, bytes([ord(c)]))

def set_rgb(r, g, b):
    i2c.writeto_mem(RGB_ADDRESS, 0x00, b'\x00')  # mode1
    i2c.writeto_mem(RGB_ADDRESS, 0x01, b'\x00')  # mode2
    i2c.writeto_mem(RGB_ADDRESS, 0x08, b'\xaa')  # enable LEDs
    i2c.writeto_mem(RGB_ADDRESS, 0x04, bytes([r]))
    i2c.writeto_mem(RGB_ADDRESS, 0x03, bytes([g]))
    i2c.writeto_mem(RGB_ADDRESS, 0x02, bytes([b]))
    
adc = ADC(26)  # GPIO26 = ADC0
Umax = 6.0

def lire_tension():
    lecture = adc.read_u16()
    tension = (lecture / 65535) * 3.3  # Conversion en volts
    return tension

set_rgb(255, 255, 255)

while True:
    lcd_write(0x01)  # Clear the display
    utime.sleep_ms(2)  # Wait for clear to finish
    U = lire_tension()
    pourcentage = (U / Umax) * 100
    lcd_set_text(" Voltage: {:.2f}V\n Bright: {:>5.1f}%".format(U, pourcentage))
    print(" Voltage PV: {:.2f}V\nBrightness:{:>5.1f}%".format(U, pourcentage))
    utime.sleep(1)
