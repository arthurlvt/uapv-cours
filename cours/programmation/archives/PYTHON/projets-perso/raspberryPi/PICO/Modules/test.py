from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

cardWrite = SimpleMFRC522()
try:
    text = raw_input('Enter data for writing to card')
    print('place your tag to write: ')
    cardWrite.write(text)
    print('Ecriture réalisée !')