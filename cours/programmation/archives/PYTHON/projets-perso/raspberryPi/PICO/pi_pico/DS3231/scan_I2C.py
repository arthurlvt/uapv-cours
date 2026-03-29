from machine import I2C, Pin
import utime

# Initialisation de l'I2C avec une fréquence de 100 kHz
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

DS3231_ADDRESS = 0x68  # Adresse du DS3231

# Fonction pour convertir les valeurs BCD en décimal
def bcd_to_dec(bcd):
    return (bcd // 16) * 10 + (bcd % 16)

# Fonction pour définir l'heure sur le DS3231
def set_rtc_time(hour, minute, second, day, month, year, weekday):
    # Convertir les valeurs en BCD
    second_bcd = (second // 10) << 4 | (second % 10)
    minute_bcd = (minute // 10) << 4 | (minute % 10)
    hour_bcd = (hour // 10) << 4 | (hour % 10)
    day_bcd = (day // 10) << 4 | (day % 10)
    month_bcd = (month // 10) << 4 | (month % 10)
    year_bcd = ((year - 2000) // 10) << 4 | ((year - 2000) % 10)
    weekday_bcd = (weekday // 10) << 4 | (weekday % 10)

    # Écrire les valeurs dans le DS3231
    i2c.writeto_mem(DS3231_ADDRESS, 0x00, bytearray([second_bcd, minute_bcd, hour_bcd, weekday_bcd, day_bcd, month_bcd, year_bcd]))

# Définir une date et une heure (exemple : 10:30:00, le 12 août 2024, lundi)
set_rtc_time(18, 37, 40, 16, 11, 2024, 7)  # 1 = Lundi

# Vérifier si l'heure est correctement programmée
while True:
    try:
        # Lire l'heure du DS3231 (7 premiers octets)
        time_data = i2c.readfrom_mem(DS3231_ADDRESS, 0x00, 7)
        second = bcd_to_dec(time_data[0] & 0x7F)  # Masquer le bit de l'alerte
        minute = bcd_to_dec(time_data[1])
        hour = bcd_to_dec(time_data[2] & 0x3F)  # Masquer les bits AM/PM
        weekday = bcd_to_dec(time_data[3])
        day = bcd_to_dec(time_data[4])
        month = bcd_to_dec(time_data[5])
        year = bcd_to_dec(time_data[6]) + 2000  # Ajouter 2000 pour obtenir l'année complète
        
        # Afficher l'heure lue sous un format lisible
        print("Heure: {:02}:{:02}:{:02} - Jour: {:02}/{:02}/{:04} - Semaine: {}".format(
            hour, minute, second, day, month, year, ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"][weekday - 1]
        ))
    except Exception as e:
        print("Erreur lors de la lecture:", e)

    utime.sleep(1)  # Délai de 1 seconde
