# TO MAKE THIS COMPONENT FUNCTIONAL, PUT OFF ALL SWITCHES

import sys # Importing sys library
import time # Importing time library
from mfrc522 import SimpleMFRC522 # Importing mfrc522 library to use RFID reader
reader = SimpleMFRC522()
import warnings # Importing warnings to remove useless warnings
warnings.filterwarnings("ignore")

try:
  for i in range(1):
    print('Please put your badge on RFID reader')
    authenticated = False
    while not authenticated:
      try:
        id, text = reader.read()
        authenticated = True
      except Exception as e:
        print(f'Auth Error: {e}')
        time.sleep(1)
    
    if text.strip():
      print(f'Tag ID: {id}')
      if id == '123456654321':
        name = 'John'
        print('Bienvenue', name, '!')
      else:
        print(f'ID: {id}, Content: {text}')
    else:
      print('Invalid tag ! Rebooting in progress...')
      sys.exit(0)

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
        