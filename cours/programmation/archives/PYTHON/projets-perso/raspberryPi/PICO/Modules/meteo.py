#!/usr/bin/python
import sys
import time
import smbus
import Adafruit_DHT
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

if(GPIO.RPI_REVISION == 1):

  bus = smbus.SMBus(0)

else:

  bus = smbus.SMBus(1)

lcd_columns = 16 

lcd_rows = 2
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
lcd.set_backlight(0) 
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
t=str(temperature)
h=str(humidity)

#Luxmetre
class LightSensor():

  def convertToNumber(self, data):

    return (int((data[1] + (256 * data[0])) / 1.2)) #valeur constructeur

  def readLight(self):

    data = bus.read_i2c_block_data(0x5C,0x10) #0x5C = adresse du capteur ; 0x10 = standard de mesure
    return self.convertToNumber(data)

#Temperature & Humidite
def dht():

  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  t=str(temperature)
  h=str(humidity)
  if humidity is not None and temperature is not None:

  lcd.message(‘T=’+t+’*C H=’+h+’%’)

#Main
def main():

  print “En etat de marche… \nCTRL+C ou Z pour arreter”
  while True:

    GPIO.cleanup()
    dht()

    #Lumiere
    sensor = LightSensor()
    l=str(sensor.readLight())
    lcd.message(‘\n’+l+’ lux’)

    time.sleep(2)
    lcd.clear()

#Run
if __name__ == ‘__main__’:
  main()
