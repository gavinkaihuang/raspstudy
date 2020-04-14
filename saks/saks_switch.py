import time
import sys
from sakshat import SAKSHAT
import subprocess #python3 replace commands package with subprocess

'''
通过树莓派获取CPU 和GPU的温度

'''
def dip_switch_status_changed_handler(status):
    '''
    called while the status of dip switch changed
    :param status: current status
    :return: void
    '''
    print('on_dip_switch_status_changed:')
    print(status)
    pass

def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    print('tact_event_handler')
    print("%d - %s" % (pin, status))

if __name__ == '__main__':
    saks = SAKSHAT()
    saks.dip_switch_status_changed_handler = dip_switch_status_changed_handler
    saks.tact_event_handler = tact_event_handler

    while True:
        time.sleep(1)