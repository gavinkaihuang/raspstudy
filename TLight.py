#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import sys

"""
study url: https://my.oschina.net/qnloft/blog/1819817
"""

def first_light(arg):
    print("Run fist light %d" % arg)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, True)
    time.sleep(3)
    GPIO.output(11, False)
    GPIO.cleanup()

def flash_light():
    print("Now try to flash light ")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    i = 0
    try:
        while True:

            if i > 10:
                break
            GPIO.output(11, True)
            time.sleep(0.5)
            GPIO.output(11, False)
            time.sleep(0.5)
            i += 1

    finally:
        GPIO.cleanup()

def control_light_strong():
    led_pin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)

    pwm_led = GPIO.PWM(led_pin, 500)
    pwm_led.start(100)

    try:
        while True:
            duty_s = input("请输入你要的亮度（0-100）：")
            duty = int(duty_s)
            pwm_led.ChangeDutyCycle(duty)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    for arg in sys.argv:
        print("param %s" % arg)

    arg1 = sys.argv[0]
    if arg1:
        arg1 = 1
    else:
        arg1 = 0

    first_light(arg1)

    # flash_light()
    #
    # control_light_strong()
    # pass
