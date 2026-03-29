import machine
from machine import Pin, PWM
import time

TRIG = machine.Pin(17,machine.Pin.OUT)
ECHO = machine.Pin(16,machine.Pin.IN)
led = Pin(15, Pin.OUT)
led_2 = Pin(25, Pin.OUT)
servo_pin = PWM(Pin(12))
servo_pin.freq(50)

def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while not ECHO.value():
        pass
    time1 = time.ticks_us()
    while ECHO.value():
        pass
    time2 = time.ticks_us()
    during = time.ticks_diff(time2,time1)
    return during * 340 / 2 / 10000

def set_angle(angle):
    duty = int(1024 * (0.5 + angle / 180 * 2.5))  # Conversion angle en PWM
    servo_pin.duty_u16(duty)

while True:
    dis = distance()
    led_2.value(2)
    if dis <= 20:
        led.value(1)
        print ('Someone or Something got detected, Distance: %.2f cm' % dis)
        time.sleep(1)
        for i in range(1):
            set_angle(0)      # Angle 0°
            time.sleep(1)
            set_angle(90)    # Angle 180°
            time.sleep(1)
    else:
        led.value(0)
        
    

