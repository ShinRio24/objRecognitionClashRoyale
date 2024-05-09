import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('Bluestacks App Player')
skelVision = Vision('skel2.jpg')


loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    points = skelVision.find(screenshot, 0.07, 'rectangles')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')