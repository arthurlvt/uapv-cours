#import necessary libraries
import RPi.GPIO as GPIO
import time
import smbus

#check RPI card revision
if(GPIO.RPI_REVISION == 1):
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)

#The LightSensor class
class LightSensor():
    def __init__(self):
        #define some constants from the datasheet
        self.DEVICE = 0x5c #default device I2C address
        self.POWER_DOWN = 0x00 #no active state
        self.POWER_ON = 0x01 #power on
        self.RESET = 0x07 #reset data register value
        #start measurement at 4 Lux
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        #start measurement at 1 Lux
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        #start measurement at 0.5 Lux
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        #start measurement at 1 Lux
        #device is automatically set to power down mode after measurement
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        #start measurement at 0.5 Lux
        #device is automatically set to power down mode after measurement
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        #start measurement at 4 Lux
        #device is automatically set to power down mode after measurement
        self.ONE_TIME_LOW_RES_MODE = 0x23
        
    def convertToNumber(self, data):
        #Simple function to convert 2 Bytes of data
        #into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)
    
    def readLight(self):
    
        data = bus.read_i2c_block_data(self.DEVICE,self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convertToNumber(data)

#main code
def main():
    sensor = LightSensor()
    try:
        while True:
            print("Light Level : " + str(sensor.readLight()) + " lx")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main()
