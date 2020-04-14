# coding=utf-8
import RPi.GPIO as GPIO
import time

'''
声音传感器模块
'''

GPIO_PIN = 4
GPIO_OUT = 25

def callback_fun_soundOccurred(input_pint):
    print("callback_fun_soundOccurred: ", str(input_pint))

def detct():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    GPIO.setup(GPIO_OUT, GPIO.OUT)

    try:
        while True:       
            if GPIO.input(GPIO_PIN) == 0:
                GPIO.output(GPIO_OUT, GPIO.HIGH)
                time.sleep(1)
            else:
                GPIO.output(GPIO_OUT, GPIO.LOW)
            
    finally:
        GPIO.cleanup()
    

if __name__ == '__main__':
    detct()