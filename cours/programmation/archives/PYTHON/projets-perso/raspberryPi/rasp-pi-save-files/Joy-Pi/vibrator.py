#import necessary libraries
import RPi.GPIO as GPIO 
import time
#define pins
vibration_pin = 13
#set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)
#setup button_pin as input and buzzer_pin as output
GPIO.setup(vibration_pin, GPIO.OUT)
try:
    while True:
        #activate vibration
        GPIO.output(vibration_pin, GPIO.LOW)
        #wait haf a second
        time.sleep(0.5)
        #stop vibration
        GPIO.output(vibration_pin, GPIO.HIGH)
        #close relay
        #wait haf a second
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    
# COMMUTATEUR 1 DU BLOC DROIT
