#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import sys

"""
测试距离传感器， 并点亮灯
"""

Trig_Pin = 7    #信号发送口使用7号GPIO
Echo_Pin = 22   #信号接收口使用22号GPIO
Light_Pin = 11   #信号灯接收口使用7号GPIO

def init():
    GPIO.setmode(GPIO.BOARD)

def trig_light():
    GPIO.setup(Light_Pin, GPIO.OUT)
    GPIO.output(Light_Pin, True)
    time.sleep(0.003)
    GPIO.output(Light_Pin, False)


def get_distance():
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
    init()

    try:
        while True:
            # print('-------')
            dis = get_distance()
            trig_light()
            print('Distance:%0.2f cm' % dis)
            time.sleep(1)
    except KeyboardInterrupt:
        # GPIO.cleanup()
        pass
    finally:
        GPIO.cleanup()