import RPi.GPIO as GPIO

import time

"""
study url: https://my.oschina.net/qnloft/blog/1819817
"""

def first_light():
    print("Run fist light")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, True)
    time.sleep(8)
    GPIO.output(11, False)
    GPIO.cleanup()

def flash_light():
    print("Now try to flash light ")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    i = 0
    try:
        while True:

            if i > 10:
                break
            GPIO.output(11, True)
            time.sleep(0.5)
            GPIO.output(11, False)
            time.sleep(0.5)
            i += 1

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    first_light()

    flash_light()
    pass
