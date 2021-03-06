#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import sys

"""
超声波测试距离传感器
"""

Trig_Pin = 4    #信号发送口使用4号GPIO
Echo_Pin = 25   #信号接收口使用25号GPIO


def getDistance():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo_Pin, GPIO.IN)
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2




if __name__ == '__main__':
    # for arg in sys.argv:
    #     print("param %s" % arg)

    try:
        while True:
            print('-------')
            dis = getDistance()
            print('Distance:%0.2f cm' % dis)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()