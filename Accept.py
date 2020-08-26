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

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


while True:
    print(pointToClick)


    print("test")
    color = [getPixel(p1), getPixel(p2), getPixel(p3), getPixel(p4)]
    if color[0] == Colors and color[1] == Colors and color[2] == Colors and color[3] == Colors:
        win32api.SetCursorPos(pointToClick)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pointToClick[0], pointToClick[1], 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pointToClick[0], pointToClick[1], 0, 0)
    if keyboard.is_pressed('q'):
        exit(1)
