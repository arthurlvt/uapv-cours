import RPi.GPIO as GPIO
import time

IN1 = 6
IN2 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def tourner_avant():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    
def tourner_arriere():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    
def stop_motor():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    

try:
    while True:
        print('Tourne en avant')
        tourner_avant()
        time.sleep(5)
        
        print('Tourne en arrière')
        tourner_arriere()
        time.sleep(5)
        
        print('Arrêt du moteur')
        stop_motor()
        time.sleep(5)
        
except KeyboardInterrupt:
    print('Arrêt par user')
finally:
    GPIO.cleanup()
    