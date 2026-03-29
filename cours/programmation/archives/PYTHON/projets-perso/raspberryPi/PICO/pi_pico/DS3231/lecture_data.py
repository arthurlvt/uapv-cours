import utime
import machine
from machine import Pin, I2C

class DS3231_I2C:
    ADDRESS = 0x68  # Adresse I2C du DS3231
    REGISTER = 0x00  # Registre à partir duquel commencer la lecture
    
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.reg = 0x00
    
    def set_time(self, NowTime):
        """
        Programme l'heure et la date sur le DS3231.
        """
        try:
            self.i2c.writeto_mem(int(self.addr), int(self.reg), NowTime)
            print("Heure et date programmées avec succès.")
        except OSError as e:
            print("Erreur lors de la programmation de l'heure:", e)
    
    def read_time(self):
        """
        Lit l'heure et la date à partir du DS3231.
        Retourne un tableau de 7 éléments contenant les données du RTC.
        """
        try:
            # Lecture des 7 premiers octets (secondes, minutes, heures, jour, mois, année, semaine)
            data = self.i2c.readfrom_mem(int(self.addr), int(self.reg), 7)
            print("Données brutes du RTC:", data)  # Afficher les données brutes
            if len(data) == 7:
                return data
            else:
                print(f"Erreur : nombre de données incorrect. Taille retournée: {len(data)}")
                return None
        except OSError as e:
            print("Erreur lors de la lecture du RTC:", e)
            return None

# Fonction de conversion BCD en décimal
def bcd_to_dec(bcd):
    return (bcd & 0x0F) + ((bcd >> 4) * 10)

# Configuration de l'I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Remplacez les broches si nécessaire
rtc = DS3231_I2C(i2c)  # Créer une instance du module RTC DS3231

# Fonction pour lire et afficher l'heure et la date
def read_time():
    # Lire l'heure actuelle du DS3231
    t = rtc.read_time()  # Cela retourne un tableau de 7 valeurs [secondes, minutes, heures, jour, mois, année, semaine]
    
    if t is not None:
        # Vérifier la taille des données avant de tenter d'y accéder
        if len(t) < 7:
            print("Erreur: Données insuffisantes pour lire l'heure et la date.")
            return
        
        # Convertir les valeurs BCD en décimal
        second = bcd_to_dec(t[0])
        minute = bcd_to_dec(t[1])
        hour = bcd_to_dec(t[2])
        day = bcd_to_dec(t[3])
        month = bcd_to_dec(t[4])
        year = bcd_to_dec(t[5]) + 2000  # Ajouter 2000 pour l'année
        week_day = t[6]

        # Formater l'heure et la date
        time_str = "{:02}:{:02}:{:02}".format(hour, minute, second)
        date_str = "{:02}/{:02}/{}".format(day, month, year)
        
        # Afficher l'heure et la date
        print("Heure: ", time_str)
        print("Date: ", date_str)
        print("Semaine: ", ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"][week_day])

# Boucle principale pour lire et afficher l'heure toutes les secondes
while True:
    print("Lecture de l'heure...")
    read_time()  # Lire et afficher l'heure
    utime.sleep(1)  # Attendre une seconde avant la prochaine lecture
