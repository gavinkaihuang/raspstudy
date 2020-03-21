#!/usr/bin/python
# coding=utf-8
# 注意本程序是python3！！！
import RPi.GPIO as GPIO
import time


def driver():
    print("-----start driver")
    pin_no = 23
    # 初始化一个空的列表用来存放时序数据
    data = [0 for i in range(40)]
    j = 0
    # 传感器上电后，要等待1s以越过不稳定状态
    GPIO.setmode(GPIO.BOARD)
    time.sleep(1)
    # 先向传感器发送开始信号，握手-LOW-
    GPIO.setup(pin_no, GPIO.OUT)
    GPIO.output(pin_no, GPIO.LOW)
    print("-----start driver 1")
    # 主机把总线拉低必须大于18毫秒，这里采用20毫秒
    time.sleep(0.02)
    # 然后主机拉高并延时等待传感器的响应
    GPIO.output(pin_no, GPIO.HIGH)
    # 等待传感器的握手响应信号和数据信号
    GPIO.setup(pin_no, GPIO.IN)
    print("-----start driver 2")
    # 总线为低电平，说明传感器发送响应信号，80us低电平
    while GPIO.input(pin_no) == GPIO.LOW:
        print("-----start driver 2.1 GPIO.LOW")
        continue
    # 然后传感器再把总线拉高80us，然后才准备发送数据
    while GPIO.input(pin_no) == GPIO.HIGH:
        print("-----start driver 2.2 GPIO.HIGH")
        continue
    # 开始发送数据
    # 一次完整的数据为40bit，高位先出
    # 8bit湿度整数数据+8bit湿度小数数据+8bit温度整数数据+8bit温度小数数据+8bit校验和
    while j < 40:
        print("-----start driver 3")
        k = 0
        # 每一位的起始信号，都以50us低电平开始
        while GPIO.input(pin_no) == GPIO.LOW:
            continue
        # 每一位的数值信号，高电平的长短决定了数据位是0还是1。
        while GPIO.input(pin_no) == GPIO.HIGH:
            # 需要知道每次循环的耗时，才能知道k < x是表示0
            k += 1
            if k > 100:
                break
        # 高电平持续26-28us表示0， 高电平持续70us表示1
        if k < 8:
            data[j] = 0
        else:
            data[j] = 1
        j += 1
    print(data)
    return data


def compute(data):
    humidity_bit = data[0:8]  # 分割数据
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = int(''.join([str(x) for x in humidity_bit]), 2)  # 将二进制转十进制
    humidity_point = int(''.join([str(x) for x in humidity_point_bit]), 2)
    temperature = int(''.join([str(x) for x in temperature_bit]), 2)
    temperature_point = int(''.join([str(x) for x in temperature_point_bit]), 2)
    check_num = int(''.join([str(x) for x in check_bit]), 2)
    # print('温度：%d  湿度：%d' %(temperature+temperature_point,humidity+humidity_point/10))
    sum = humidity + humidity_point + temperature + temperature_point
    GPIO.cleanup()
    # 校验数据准确性，并循环打印温湿度信息
    while sum == check_num:
        print('数据正常 温度：%d℃   湿度：%d%%' % (temperature, humidity))
        time.sleep(3)
        compute(driver())
    else:
        print("警告！接收数据不准确！接收数据之和是%d,校验码为%d。正在重新接收。。。。" % (sum, check_num))
        time.sleep(3)
        compute(driver())


if __name__ == "__main__":
    compute(driver())