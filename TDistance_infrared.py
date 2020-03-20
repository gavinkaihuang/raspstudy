# coding=utf-8
import RPi.GPIO as GPIO
import time

def work():
    GPIO.setmode(GPIO.BOARD)
    # 定义引脚
    GPIO_PIN = 35
    # 设置引脚为输入
    GPIO.setup(GPIO_PIN, GPIO.IN)

    while True:
        # 当有障碍物时，传感器输出低电平，所以检测低电平
        if GPIO.input(GPIO_PIN) == 0:
            print("有障碍物")
            time.sleep(1)
        else:
            print("距离安全")
            time.sleep(1)

if __name__ == '__main__':
    work()