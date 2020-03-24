import time
import sys
from sakshat import SAKSHAT
import subprocess #python3 replace commands package with subprocess
import Adafruit_DHT

if __name__ == '__main__':

    saks = SAKSHAT()
    saks.saks_gpio_init()
    sensor = Adafruit_DHT.DHT11
    pin = 24
    hu, temp = Adafruit_DHT.read_retry(sensor, pin)
    print('温度:{0:0.1f}°C 湿度:{1:0.1f}%'.format(temp, hu))

    
    try:
        print('开始测量温度')
        # 循环
        while True:
            try:
                hu, temp = Adafruit_DHT.read_retry(sensor, pin)
                print('温度:{0:0.1f}°C 湿度:{1:0.1f}%'.format(temp, hu))
                time.sleep(2)
            except RuntimeError as e:
                print("error\n{0}".format(e))
                time.sleep(10)
            except:
                print("error\nFailed to read sensor data!")
                time.sleep(10)
    finally:
        print("clean up in finally")
        saks.saks_gpio_init()