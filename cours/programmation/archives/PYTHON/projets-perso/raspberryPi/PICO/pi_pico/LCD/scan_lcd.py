from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4))
print("I2C scan:", [hex(i) for i in i2c.scan()])
