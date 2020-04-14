import RPi.GPIO as GPIO
import time

IN=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN,GPIO.IN)

while True:
    in_value = GPIO.input(IN)
    time.sleep(1)
    print (in_value)
