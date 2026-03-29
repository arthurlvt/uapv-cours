import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70) 

segment.begin()

print ("CTRL+C pour stopper .") 

try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    segment.clear()
    # Affichage des heures
    segment.set_digit(0, int(hour / 10))
    segment.set_digit(1, hour % 10)
    # Affichage des minutes
    segment.set_digit(2, int(minute / 10))
    segment.set_digit(3, minute % 10)
    
    # Indique les secondes
    segment.set_colon(second % 2)              
    # Mettre l'affichage à jour
    segment.write_display()

    # Attend une seconde
    time.sleep(1)
except KeyboardInterrupt:
    segment.clear()
    segment.write_display()