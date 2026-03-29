import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11
DHTpin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

humidity, temperature = Adafruit_DHT.read(sensor, DHTpin)
        
if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature}C | Humidity: {humidity}%')
else:
    print('Reading error ! Please try again :)')
    time.sleep(2)
            
