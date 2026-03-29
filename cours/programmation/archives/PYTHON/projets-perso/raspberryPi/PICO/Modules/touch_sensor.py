#!/usr/bin/env python
# -*- coding: utf-8 -*-


from RPi import GPIO
import signal

TOUCH = 11

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TOUCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def do_smt(channel):
    print("Touch wurde erkannt")

def main():
    setup_gpio()
    try:
        GPIO.add_event_detect(TOUCH, GPIO.FALLING, callback=do_smt, bouncetime=200)
        signal.pause()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()

# TOUS LES COMMUTATEURS SUR OFF