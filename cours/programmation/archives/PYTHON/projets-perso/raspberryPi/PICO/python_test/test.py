import RPi.GPIO as GPIO
import sys as sys
import time as time

LED = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.setwarnings(False)

pwm_led = GPIO.PWM(LED, 1000)
pwm_led.start(0)

try:
    while True:      
        for duty_cycle in range(100, -1, -5):
            pwm_led.ChangeDutyCycle(duty_cycle)
            print(f'Intensité LED: {duty_cycle}%')
            time.sleep(0.1)
            
            
except KeyboardInterrupt:
    pass
    
    
finally:
    pwm_led.stop()
    GPIO.cleanup()
            
                       
                       


