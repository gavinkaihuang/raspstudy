import time
import sys
from sakshat import SAKSHAT

def timer():
    while True:
        time_value = time.strftime("%H.%M", time.localtime())
        saks.digital_display.show(time_value)
        time.sleep(1)

if __name__ == '__main__':

    saks = SAKSHAT()
    timer()