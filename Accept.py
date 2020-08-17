import ctypes
from ctypes import windll
import keyboard
import win32api, win32con
from win32api import GetSystemMetrics

Colors = 5287756

p1 = (int(GetSystemMetrics(0) * 0.4453125), int(GetSystemMetrics(1) * 0.53125))
p2 = (int(GetSystemMetrics(0) * 0.5546875), int(GetSystemMetrics(1) * 0.53125))
p3 = (int(GetSystemMetrics(0) * 0.4453125), int(GetSystemMetrics(1) * 0.5972222))
p4 = (int(GetSystemMetrics(0) * 0.5546875), int(GetSystemMetrics(1) * 0.5972222))

pointToClick = (int(((p2[0] - p1[0]) / 2.0) + p1[0]), int(((p3[1] - p1[1]) / 2.0) + p1[1]))

SendInput = ctypes.windll.user32.SendInput
dc = windll.user32.GetDC(0)

PUL = ctypes.POINTER(ctypes.c_ulong)


def getPixel(Point):
    return windll.gdi32.GetPixel(dc, Point[0], Point[1])


while True:
    color = [getPixel(p1), getPixel(p2), getPixel(p3), getPixel(p4)]
    if color[0] == Colors and color[1] == Colors and color[2] == Colors and color[3] == Colors:
        win32api.SetCursorPos(pointToClick)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pointToClick[0], pointToClick[1], 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pointToClick[0], pointToClick[1], 0, 0)
    if keyboard.is_pressed('q'):
        exit(1)
