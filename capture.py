import subprocess
import cv2
import numpy
from matplotlib import pyplot
from subprocess import Popen

method = cv2.TM_CCOEFF_NORMED

adbconsole = r'D:\Application\LDPlayer\LDPlayer4.0\adb.exe'


def pull_capture():
    p = Popen([adbconsole, 'pull', '/sdcard/screen.png', 'D:\Application\LDPlayer\LDPlayer4.0\screen'],
              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()

    print(output)


def capture():
    p = Popen([adbconsole, 'shell', 'screencap', '-p', '/sdcard/screen.png'],
              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()

    print(output)


def check_capture():
    small_image = cv2.imread(r'C:\Users\Root\Desktop\ADB Capture\play_now.png', 0)
    large_image = cv2.imread(r'D:\Application\LDPlayer\LDPlayer4.0\screen\screen.png')
    large_image_gray = cv2.cvtColor(large_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(small_image, large_image_gray, method)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    threshold = 0.8
    flag = False
    loc = numpy.where(result >= threshold)
    for pt in zip(*loc[::-1]):
        flag = True

    (start_x, start_y) = maxLoc
    end_x = start_x + small_image.shape[1]
    end_y = start_y + small_image.shape[0]

    center_x = start_x + (end_x/2)
    center_y = start_y + (end_y/2)
    print(flag)
    print(center_x)
    print(center_y)

