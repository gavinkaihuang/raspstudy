#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT



# 定义sensor型号为DHT22
sensor = Adafruit_DHT.DHT22

def work():
    GPIO.setmode(GPIO.BCM)
    # BCM number
    pin = 26
    try:
        print('开始测量温度')
        # 循环
        while True:
            try:
                hu, temp = Adafruit_DHT.read_retry(sensor, pin)
                # print('temperature:{0:0.1f}°C humidity:{1:0.1f}%'.format(temp,hu))
                print('温度:{0:0.1f}°C 湿度:{1:0.1f}%'.format(temp, hu))
                time.sleep(2)
            except RuntimeError as e:
                print("error\n{0}".format(e))
            except:
                print("error\nFailed to read sensor data!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    work()