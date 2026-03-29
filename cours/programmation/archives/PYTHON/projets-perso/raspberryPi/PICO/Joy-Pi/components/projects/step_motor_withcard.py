import RPi.GPIO as GPIO
import time

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

sequence = [
    [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
    [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
    [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
    [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
    [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
    [GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.HIGH],
]

def step_motor(steps):
    for _ in range(steps):
        for step in sequence:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(0.001)
            
try:
    while True:
        step_motor(512)
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup GPIO.output(IN1, step[0])
              
            