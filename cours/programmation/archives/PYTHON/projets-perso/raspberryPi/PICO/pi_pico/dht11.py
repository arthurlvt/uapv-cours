from machine import Pin
import utime
from DHT11 import DHT11  # Assurez-vous que DHT11.py est présent

# Initialiser le capteur DHT11 sur le GPIO 11
dht_sensor = DHT11(Pin(11))  # Remplacez 11 par la broche à laquelle votre DHT est connecté

while True:
    # Lire la température et l'humidité
    humidity, temperature = dht_sensor.read()
    
    # Vérifiez si la lecture est valide
    if humidity is not None and temperature is not None:
        print(f"Température: {temperature}°C, Humidité: {humidity}%")  # Afficher les valeurs
    else:
        print("Échec de la lecture du capteur. Essayez encore !")
    
    utime.sleep(2)  # Attendre 2 secondes avant de lire à nouveau

