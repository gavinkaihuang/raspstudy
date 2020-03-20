#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT



# 定义sensor型号为DHT22
sensor = Adafruit_DHT.DHT11

def work():
    GPIO.setmode(GPIO.BOARD)
    # BCM number
    pin = 16
    try:
        print('开始测量温度')
        # 循环
        while True:
            try:
                print('------start-----')
                hu, temp = Adafruit_DHT.read_retry(sensor, pin)
                print(hu)
                print(temp)
                print('----read value---')
                # print('temperature:{0:0.1f}°C humidity:{1:0.1f}%'.format(temp,hu))
                print('温度:{0:0.1f}°C 湿度:{1:0.1f}%'.format(temp, hu))
                time.sleep(2)
            except RuntimeError as e:
                print("error\n{0}".format(e))
            except:
                print("error\nFailed to read sensor data!")
    finally:
        print("clean up in finally")
        GPIO.cleanup()

if __name__ == '__main__':
    work()
