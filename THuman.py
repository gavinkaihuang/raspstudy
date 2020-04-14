#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

HC-SR501 人体感应模块

'''

import RPi.GPIO as GPIO
import time
import sys



def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)

 
def detct():
    while (True):
        if GPIO.input(4) == True:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) , "  Attention: 有人靠近!")
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) , "  一切如此安静!")
        time.sleep(1) #每6秒检查一次


if __name__ == '__main__':
    time.sleep(2)
    init()
    detct()