#Connect LED to GPIO 4 and 17 pins

import RPi.GPIO as GPIO #import library
import time
pinNum = 4
pin2Num = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum,GPIO.OUT)
GPIO.setup(pin2Num,GPIO.OUT)

while True:
  GPIO.output(pinNum,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(pinNum,GPIO.LOW)
  GPIO.output(pin2Num,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(pin2Num,GPIO.LOW)
  
