### 1, study for raspberry

##### 1. TLight.py
    study url: https://my.oschina.net/qnloft/blog/1819817

##### 2. TDistance.py
![avatar](./images/TDistance.jpeg)
    study url: http://zhaoxuhui.top/blog/2018/12/10/RaspberrySensors.html

##### 3. TDistance_light.py
    结合灯和距离传感器联动

##### 4. TDistance_infrared.py
![avatar](./images/TDistance_infrared.jpeg)
    红外传感器测距
    1 VCC 外接3.3V-5V电压（可以直接与5v单片机和3.3v单片机相连）
    2 GND 外接GND
    3 OUT 小板数字量输出接口（0和1）
    study url: http://zhaoxuhui.top/blog/2018/12/10/RaspberrySensors.html

##### 5. THuman.py
    HC-SR501 人体感应模块

##### 6. TLIRC.py
    打印红外接收器的按键编码

##### 7. TSound.py
![avatar](./images/TSound.jpeg)
    声音传感器 STC89C52
    传感器灵敏度调整，按图上顺时针为灵敏度低，逆时针为灵敏度高


### 2, saks 扩展板代码测试
![avatar](./images/saks.jpeg)

##### 1.  saks_gpio.py 
    将温度传感器连接到扩展板的GPIO24口，读取温度和湿度

##### 2. saks_switch.py 
    SAKS板的按钮和拨动开关监控

##### 3.  saks_tempture.py 
    SAKS板接入板子默认传感器（ds18b20）测试温度 显示温度为-128.0 确认是否传感器有问题

##### 4.  saks_timer.py 
    SAKS板计时器

##### 5.  saks_main.py 
    尝试按钮切换温度和湿度


##### 6.  saks_showtempwetinfo.py 
    通过不同参数显示温度和湿度
    exe： python3 saks_showtempwetinfo.py 1 //显示温度
        python3 saks_showtempwetinfo.py 2 //显示湿度


