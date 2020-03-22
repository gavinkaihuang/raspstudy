import time
import sys
from sakshat import SAKSHAT

def loop_lights():
    saks.ledrow.off()
    for number in range(8):
        saks.ledrow.on_for_index(number)
        time.sleep(0.05)
    for number in range(8):
        saks.ledrow.off_for_index(8 - number)
        time.sleep(0.05)


def clean_lights():
    # print("clean_lights ")
    row = [False, False, False, False, False, False, False, False]
    saks.ledrow.set_row(row)

def light_low(index):
    index_value = int(index)
    # print("light_low %d" % index_value)
    row = [False, False, False, False, False, False, False, False]
    lenth = len(row)
    num = 0
    for num in range(index_value):
        # print(index_value)
        row[lenth - num - 1] = True
        # if (num == index - 1):
    saks.ledrow.set_row(row)

    time.sleep(0.2)
    flash_number = lenth - index_value
    # print("lights value is ", row, " flash_number %d" % flash_number)
    saks.ledrow.off_for_index(flash_number)



def show_seconds(time_second):
    # try:
    # print("second is " , time_second)
    second = int(time_second)

    if second == 0:
        # clean_lights()

        loop_lights()

    else:
        index = second / 10 + 1
        light_low(index)
        # elif second < 10:
        #     index = 1
        # elif second < 20:
        #     index = 2
        # elif second < 30:
        #     index = 3
        # elif second < 40:
        #     index = 4
        # elif second < 50:
        #     index = 5
        # elif second < 60:
        #     index = 6


    # except BaseException:
    #     print(BaseException)
    #     pass



def timer():
    while True:
        time_value = time.localtime()
        time_second = time.strftime("%S", time_value)
        time_show = time.strftime("%H.%M", time_value)
        saks.digital_display.show(time_show)

        show_seconds(time_second)
        time.sleep(1)





if __name__ == '__main__':

    saks = SAKSHAT()
    timer()