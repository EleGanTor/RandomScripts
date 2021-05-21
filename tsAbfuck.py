import win32api, win32con
from pynput.keyboard import Key, Controller
import time
import keyboard
import pyautogui
from _thread import start_new_thread
board = Controller()
pCreate = (282, 1381)
startAscii = 97
maxAscii = 122
canCreate = False
def getName(oldName):
    newName = oldName
    for i in range(0, len(oldName)):
        number = ord(oldName[i])
        if number < maxAscii:
            newName[i] = chr(ord(oldName[i]) + 1)
            return newName
        else:
            newName[i] = chr(startAscii)
            try:
                newName[i + 1] = chr(ord(oldName[i + 1]) + 1)
                if ord(oldName[i + 1]) < maxAscii:
                    return newName
            except IndexError:
                newName.append(chr(startAscii))
                return newName
    return newName

def ThreadWaiting():
    global canCreate
    while True:
        time.sleep(22)
        canCreate = True
        time.sleep(0.01)
        canCreate = False

if __name__ == '__main__':
    oldString = ['d', 'k']
    start_new_thread(ThreadWaiting, ())

    while True:
        if canCreate:
            #win32api.SetCursorPos(pCreate)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pCreate[0], pCreate[1], 0, 0)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pCreate[0], pCreate[1], 0, 0)
            pyautogui.click(pCreate[0], pCreate[1])
            time.sleep(0.1)
            for item in oldString:
                board.press(item)
                board.release(item)
            board.press(Key.tab)
            board.release(Key.tab)
            time.sleep(0.1)
            board.press('a')
            board.release('a')
            board.press(Key.enter)
            board.release(Key.enter)
            oldString = getName(oldString)
            canCreate = False
        if keyboard.is_pressed('q'):
            exit(1)