# from picamera import PiCamera
# from time import sleep
#
# camera = PiCamera()
#
# camera.start_preview()
# sleep(5)
# camera.stop_preview()

#!/usr/bin/python

import picamera
import time

with picamera.camera as camera:
   camera.resolution = (640, 480)
   camera.start_preview()
   time.sleep(10)
   camera.capture('/home/pi/image.jpg')
   camera.stop_preview()