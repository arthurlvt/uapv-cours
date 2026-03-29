import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pwm_gpio = 11
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

pwm.start(0)
print('Waiting for 2 seconds')
time.sleep(2)

duty = 2

while duty <= 12:
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.3)
	pwm.ChangeDutyCycle(0)
	time.sleep(0.7)
	duty = duty + 1

time.sleep(2)

print('Turning back to 90 degres for 2 seconds')
pwm.ChangeDutyCycle(7)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)
time.sleep(1.5)

print('Turning back to 0 degres')
pwm.ChangeDutyCycle(2)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
print('END')

# NE FONCTIONNE QUE SUR LES BROCHES POUR LE MOMENT
