import board
import digitalio
import busio

print('Hello Blinka !')

pin = digitalio.DigitalInOut(board.D4)
print('Digital IO Ok !')

i2c = busio.I2C(board.SCL, board.SDA)
print('I2C Ok !')

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print('SPI Ok !')

print('Done!')