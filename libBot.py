# pip install pypiwin32 playsound==1.2.2 Image numpy opencv-python
import win32gui, win32con, win32api
from playsound import playsound
from PIL import ImageGrab, ImageEnhance
import numpy as np
import time
import cv2
import os
import sys

class screenOpts:
    def __str__(self):
        return f"{self.windowName} x_min:{self.x_min} y_min:{self.y_min} x_max:{self.x_max} y_max:{self.y_max} x_len:{self.x_len} y_len:{self.y_len} dim_sum:{self.dim_sum} window:{self.window} debug:{self.debug}"

    windowName = "NoxPlayer"
    x_min = 0
    y_min = 0
    x_max = 0
    y_max = 0
    x_len = 0
    y_len = 0
    dim_sum = 0
    window = 0
    debug = 0

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

def listWindows():
    win32gui.EnumWindows( winEnumHandler, None )

def grabFragment(screenOpts,x1,y1,x2,y2):
    XrightOffset=screenOpts.x_len-x2
    YbottomOffset=screenOpts.y_len-y2
    return grabGameWindow(screenOpts,Yoffset=y1,YbottomOffset=YbottomOffset,contrast=False,Xoffset=x1,XrightOffset=XrightOffset)

def grabGameWindow(screenOpts,Yoffset=0,YbottomOffset=0,contrast=False,Xoffset=0,XrightOffset=0):
    if Yoffset + YbottomOffset >= screenOpts.y_len:
        print("ERROR - offsets bigger than total height")
        return -1
    im = ImageGrab.grab((screenOpts.x_min+Xoffset,screenOpts.y_min+Yoffset,screenOpts.x_max-XrightOffset,screenOpts.y_max-YbottomOffset), all_screens=True)
    if contrast:
        im = ImageEnhance.Brightness(im)
        im = im.enhance(1.5)
        im = ImageEnhance.Contrast(im)
        im = im.enhance(1.5)
    if screenOpts.debug != 0:
        im.save(os.getcwd() + '\\GrabGameWindow.png', 'PNG')
    return im

def findImgOnScreen(screenOpts, template_img, threshold=0.8, Yoffset=0, YbottomOffset=0, Xoffset=0, XrightOffset=0):
    img_rgb = cv2.cvtColor(np.array(grabGameWindow(screenOpts,Yoffset,YbottomOffset,Xoffset=Xoffset, XrightOffset=XrightOffset)), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_img)
    w, h = template.shape[:-1]
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    click = (0, 0)
    if len(list(zip(*loc[::-1]))):
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
            click = (pt[0] + screenOpts.x_min + Xoffset, pt[1] + screenOpts.y_min + Yoffset)
            if screenOpts.debug != 0:
                cv2.imwrite('result.png', img_rgb)
                print('found: ',click)
            break
        return click
    print(template_img + " not found on screen")
    return 0

def clickImage(sleep, template_img, threshold=0.8, Yoffset=0, YbottomOffset=0, pointerXoffset=30, pointerYoffset=30):
    counter=10
    while True:
        pointer = findImgOnScreen(screenOpts, template_img, threshold, Yoffset, YbottomOffset)
        if pointer != 0:
            pointer = (pointer[0] + pointerXoffset, pointer[1] + pointerYoffset)
            clickAbsolute(screenOpts, pointer, sleep)
            return True
        else:
            if counter <= 0:
                return False
            counter-=1
            time.sleep(1)

def clickAbsolute(screenOpts,x=(0, 0),delay=0.5,pressTime=0.05):
    updateWindow(screenOpts)
    win32api.SetCursorPos(x)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(pressTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.",x)
    time.sleep(delay)

def clickGame(screenOpts,x=(0, 0),delay=0.5,Yoffset=0,pressTime=0.05):
    clickAbsolute(screenOpts,(int(x[0])+screenOpts.x_min,int(x[1])+screenOpts.y_min+Yoffset),delay,pressTime)

def cursorPosition(screenOpts,x=(0, 0)):
    win32api.SetCursorPos((x[0]+screenOpts.x_min,x[1]+screenOpts.y_min))

def printCoords(screenOpts):
    x_absolute, y_absolute = win32api.GetCursorPos()
    x = x_absolute - screenOpts.x_min
    y = y_absolute - screenOpts.y_min
    try:
        x_proc = float(x) * 100 / screenOpts.x_len
    except ZeroDivisionError:
        x_proc = 0
    try:
        y_proc = float(y) * 100 / screenOpts.y_len
    except ZeroDivisionError:
        y_proc = 0
    print("(%d %d) (%.2f%% %.2f%%) absolute: (%d %d)" % (x, y, x_proc, y_proc, x_absolute, y_absolute))

def dimensions(screenOpts):
    print("x_min: %d y_min: %d" % (screenOpts.x_min, screenOpts.y_min))
    print("x_max: %d y_max: %d" % (screenOpts.x_max, screenOpts.y_max))
    print("x_len: %d y_len: %d" % (screenOpts.x_len, screenOpts.y_len))

def getWindow(screenOpts):
    screenOpts.window = win32gui.FindWindow(None, screenOpts.windowName)
    rect = win32gui.GetWindowRect(screenOpts.window)
    scrn = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
    windowed = 1
    if (rect == scrn):
        windowed = 0
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    screenOpts.x_min = x
    screenOpts.y_min = y
    screenOpts.x_max = x + w
    screenOpts.y_max = y + h
    if windowed==1:
        screenOpts.x_min+=2
        screenOpts.y_min+=32
        screenOpts.x_max-=40
        screenOpts.y_max-=2
    screenOpts.x_len = screenOpts.x_max - screenOpts.x_min
    screenOpts.y_len = screenOpts.y_max - screenOpts.y_min
    sum = screenOpts.x_min + screenOpts.x_max + screenOpts.y_min + screenOpts.y_max + screenOpts.x_len + screenOpts.y_len
    if (sum != screenOpts.dim_sum):
        if (windowed == 1):
            print("Window update - window mode")
        if (windowed == 0):
            print("Window update - full screen")
        dimensions(screenOpts)
        screenOpts.dim_sum = sum
        return 1
    return 0

def updateWindow(screenOpts):
    return getWindow(screenOpts)

def isWindowFocus(screenOpts):
    return screenOpts.window == win32gui.GetForegroundWindow()

def loopDelay(seconds,alarmTime = -1,alarmFile = ''):
    while True:
        if seconds==0:
            print("")
            break
        if seconds==alarmTime:
            playsound(alarmFile)
            seconds-=1
        sys.stdout.write('\r')
        sys.stdout.flush()
        print("sleeping: " + str(seconds) + "s      ", end='', flush=True)
        time.sleep(1)
        seconds-=1

def scrollUp():
    print("scrollUp")
    cursorPosition(screenOpts,(screenOpts.x_len // 2, screenOpts.y_len // 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 10000000, 0)

def fail(text):
    print("ERR: " + text)
    exit(1)
