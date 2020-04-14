import time
import sys
from sakshat import SAKSHAT
import subprocess #python3 replace commands package with subprocess

'''
通过树莓派获取CPU 和GPU的温度

'''

def get_gpu_temp():
    gpu_temp = subprocess.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8* gpu_temp)+32

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    #return float(1.8*cpu_temp)+32

if __name__ == '__main__':
    saks = SAKSHAT()
    b = saks.buzzer
    while True:
        tcpu = get_cpu_temp()
        tgpu = get_gpu_temp()
        print("cpu %3.1f; gpu %3.1f" % (tcpu, tgpu))
        print("当前室内温度:" , saks.ds18b20.temperature) #demo 显示温度为-128.0 确认是否传感器有问题
        #SAKS.digital_display.show("%3.2f" % t)
        if tcpu > 50:
            b.beepAction(0.02,0.02,30)
        time.sleep(1)


        