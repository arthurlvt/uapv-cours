from machine import I2C, Pin, ADC
import utime
from dht11_api import DHT11, InvalidChecksum, InvalidPulseCount

# --- Adresses Grove LCD ---
LCD_ADDRESS = 0x3e
RGB_ADDRESS = 0x30

# --- I2C & capteurs ---
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
sensor = DHT11(Pin(13, Pin.OUT, Pin.PULL_DOWN))
ldr = ADC(26)  # Luminosité
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Bouton de mode d'affichage
power_btn = Pin(15, Pin.IN, Pin.PULL_UP)  # Bouton d'extinction écran

# --- Variables d'état ---
display_mode = 0  # 0=temp, 1=hum, 2=lum
last_button_state = button.value()
last_power_btn_state = power_btn.value()
last_button_time = utime.ticks_ms()
last_power_time = utime.ticks_ms()
debounce_ms = 200
lcd_on = True  # État de l'écran LCD

# --- Fonctions d'affichage LCD Grove ---
def lcd_write(cmd, mode=0):
    i2c.writeto_mem(LCD_ADDRESS, mode, bytes([cmd]))

def lcd_set_text(text):
    if not lcd_on:
        return
    lcd_write(0x01)  # Clear
    utime.sleep_ms(2)
    lcd_write(0x0C)  # Display ON
    lcd_write(0x28)  # 2 lines
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            lcd_write(0xC0)
            if c == '\n':
                continue
        count += 1
        i2c.writeto_mem(LCD_ADDRESS, 0x40, bytes([ord(c)]))

def set_rgb(r, g, b):
    i2c.writeto_mem(RGB_ADDRESS, 0x00, b'\x00')
    i2c.writeto_mem(RGB_ADDRESS, 0x01, b'\x00')
    i2c.writeto_mem(RGB_ADDRESS, 0x08, b'\xaa')
    i2c.writeto_mem(RGB_ADDRESS, 0x04, bytes([r]))
    i2c.writeto_mem(RGB_ADDRESS, 0x03, bytes([g]))
    i2c.writeto_mem(RGB_ADDRESS, 0x02, bytes([b]))

def turn_off_lcd():
    set_rgb(0, 0, 0)  # Éteint rétroéclairage
    lcd_write(0x08)   # Affichage OFF

def turn_on_lcd():
    set_rgb(255, 255, 255)  # Rétroéclairage blanc
    lcd_write(0x0C)         # Affichage ON

def lire_luminosite():
    lecture = ldr.read_u16()
    tension = (lecture / 65535) * 3.3
    return (tension / 3.3) * 100  # pourcentage

# --- Couleur de départ ---
set_rgb(255, 255, 255)

# --- Boucle principale ---
while True:
    # Lecture capteurs
    try:
        temp = sensor.temperature
        hum = sensor.humidity
    except (InvalidChecksum, InvalidPulseCount):
        temp, hum = None, None

    lum = lire_luminosite()

    # Gestion bouton de changement de mode (anti-rebond)
    current_state = button.value()
    if current_state == 0 and last_button_state == 1:
        if utime.ticks_diff(utime.ticks_ms(), last_button_time) > debounce_ms:
            display_mode = (display_mode + 1) % 3
            last_button_time = utime.ticks_ms()
    last_button_state = current_state

    # Gestion bouton d'extinction écran (anti-rebond)
    current_power_state = power_btn.value()
    if current_power_state == 0 and last_power_btn_state == 1:
        if utime.ticks_diff(utime.ticks_ms(), last_power_time) > debounce_ms:
            lcd_on = not lcd_on
            if lcd_on:
                turn_on_lcd()
            else:
                turn_off_lcd()
            last_power_time = utime.ticks_ms()
    last_power_btn_state = current_power_state

    # Récupérer date/heure
    now = utime.localtime()
    date_str = "   {:02}/{:02}/{:04}".format(now[2], now[1], now[0])
    time_str = "{:02}:{:02}:{:02} |".format(now[3], now[4], now[5])

    # Choix de la donnée à afficher
    if display_mode == 0:
        info = "{}C".format(temp if temp is not None else "Err")
    elif display_mode == 1:
        info = "{}%".format(hum if hum is not None else "Err")
    else:
        info = "{:.0f}%L".format(lum)

    # Affichage sur les 2 lignes
    lcd_set_text(date_str + "\n" + time_str + " " + info)

    utime.sleep(1)
