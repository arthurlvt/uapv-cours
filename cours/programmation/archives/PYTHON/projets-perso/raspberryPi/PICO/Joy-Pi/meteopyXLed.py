import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11

led_pin = 13
DHTpin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setwarnings(False)

humidity, temperature = Adafruit_DHT.read(sensor, DHTpin)

print(f'Temperature: {temperature}C | Humidity: {humidity}%')
        
if humidity is not None and temperature is not None:
    if temperature <= 17:
        print('TEMPERATURE REACHED LOWER THAN 18 DEGRES!!')
        for x in range(0, 10):
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.1)
    else:
        GPIO.output(led_pin, GPIO.LOW)
        print('Temperature Ok')
else:
    print('Reading error ! Please try again :)')
    time.sleep(2)
            