a
import mouse
from ctypes import windll
import keyboard

dc = windll.user32.GetDC(0)

colorRed = 255
colorBlue = 16711680
colorYellow = 322559
colorPink = 16711935

pLT = (730, 360)
offsetDown = 250
offsetRight = 1020


def getPixel(Point):
    return windll.gdi32.GetPixel(dc, Point[0], Point[1])


def moveP1ToP2(point1, point2):
    mouse.drag(point1[0], point1[1], point2[0], point2[1], absolute=True, duration=0.005)


def testAndMove():
    for i in range(0, 4):
        p1 = (pLT[0], pLT[1] + offsetDown * i)
        color = getPixel(p1)
        for j in range(0, 4):
            p2 = (p1[0] + offsetRight, pLT[1] + offsetDown * j)
            color2 = getPixel(p2)
            if color == color2:
                firstClick = p1
                secondClick = p2
                moveP1ToP2(firstClick, secondClick)


if __name__ == '__main__':
    while True:
        keyboard.wait('e')
        testAndMove()
