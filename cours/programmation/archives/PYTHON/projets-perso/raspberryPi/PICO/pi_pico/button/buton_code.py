from machine import Pin
import utime
button = Pin(14, Pin.IN, Pin.PULL_UP )
while True:
    if button.value() == 0:
        print("You pressed the button!")
        utime.sleep(1)