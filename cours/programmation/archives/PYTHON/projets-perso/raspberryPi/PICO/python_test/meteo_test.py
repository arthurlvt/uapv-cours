import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11
dht_pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
    if humidity is not None and temperature is not None:
        print('Temperature: '+str(temperature)+ 'C' + '\n Humidity: '+str(humidity) + '%')
        
    else:
        print('Failed to get reading. Try Again !')
    
    time.sleep(1.0)