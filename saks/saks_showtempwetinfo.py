import time
import sys, re
from sakshat import SAKSHAT
import subprocess #python3 replace commands package with subprocess
import Adafruit_DHT

hu, temp = 0, 0
def get_temp_or_wet():
    hu1, temp1 = Adafruit_DHT.read_retry(sensor, pin)
 
    global hu
    hu = hu1
    global temp 
    temp = temp1

def show_temp_or_wet(is_temp):
    if is_temp == 1:
        value = hu
    else:
        value = temp
    temp1 = format(value, '>2.1f')
    value = "#" + str(temp1)

    #TODO 在用于计时的时候避免相互影响和覆盖，方法不科学
    loop_times = 0
    while True:
        saks.digital_display.show(value)
        time.sleep(0.2)
        loop_times += 1
        if (loop_times > 10):
            break
    
    print("value is %s" % value)

if __name__ == '__main__':
    
    show_temp = "1"
    if len(sys.argv) >= 2:
        show_temp = sys.argv[1]
        # print(show_temp)

    saks = SAKSHAT()
    sensor = Adafruit_DHT.DHT11
    pin = 24

    get_temp_or_wet()
    if show_temp == "1":
        print("show Temp")
        show_temp_or_wet(1)
    else :
        print("Show wet")
        show_temp_or_wet(2)