import time
import sys, re
from sakshat import SAKSHAT
import subprocess #python3 replace commands package with subprocess
import Adafruit_DHT

hu, temp = 0, 0
def get_temp_or_wet():

    hu1, temp1 = Adafruit_DHT.read_retry(sensor, pin)
    # print('温度:{0:0.1f}°C 湿度:{1:0.1f}%'.format(temp1, hu1))

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
    saks.digital_display.show(value)

def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    # print('tact_event_handler')
    # print("%d - %s" % (pin, status))
    if status != True:
        # print('status is true')
        return

    # print("pin %d" % pin)
    saks.ledrow.off()
    if (pin == 16):
        # print("pin 16")
        show_temp_or_wet(1)
        saks.ledrow.on_for_index(0)
    else:
        # print("pin %d" % pin)
        show_temp_or_wet(2)
        saks.ledrow.on_for_index(7)


if __name__ == '__main__':
    saks = SAKSHAT()
    sensor = Adafruit_DHT.DHT11
    pin = 24

    saks.tact_event_handler = tact_event_handler
    while True:
        get_temp_or_wet()
        time.sleep(1)