import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

time.sleep(0.25)
GPIO.output(18,GPIO.LOW)
try:
    while 1:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()