import ctypes
from ctypes import windll
import keyboard
import win32api, win32con
from win32api import GetSystemMetrics

ColorForStart = 7005463


StartingPoint = (1320, 515)


SendInput = ctypes.windll.user32.SendInput
dc = windll.user32.GetDC(0)


PUL = ctypes.POINTER(ctypes.c_ulong)

def getPixel(Point):
    return windll.gdi32.GetPixel(dc, Point[0], Point[1])

def doStart():
    while True:
        if getPixel(StartingPoint) == ColorForStart:
            return True
while True:
    if doStart():
        print("Starting now")
