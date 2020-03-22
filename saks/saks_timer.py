import time
import sys
from sakshat import SAKSHAT

def loop_lights():
    saks.ledrow.off()
    time.sleep(0.02)
    for number in range(8):
        saks.ledrow.on_for_index(number)
        time.sleep(0.02)
    for number in range(8):
        saks.ledrow.off_for_index(7 - number) #range 的范围是 0 - 7
        time.sleep(0.02)


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



def show_seconds(model, time_second):
    # try:
    # print("second is " , time_second)
    second = int(time_second)

    if second == 0:
        loop_lights()
    else:
        index = second / 10 + 1
        if (model == 0):
            light_low(index)
        else:
            saks.ledrow.off()
            saks.ledrow.on_for_index(8 - index)



def timer(model):
    while True:
        time_value = time.localtime()
        time_second = time.strftime("%S", time_value)
        time_show = time.strftime("%H.%M", time_value)
        saks.digital_display.show(time_show)

        show_seconds(time_second)
        time.sleep(1)





if __name__ == '__main__':

    model = 0
    if len(sys.argv) > 2:
        model = 1
    print("model is %d" % model)


    saks = SAKSHAT()
    timer(model)