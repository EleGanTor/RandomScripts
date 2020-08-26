// Accept.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

#include <iostream>
#include<Windows.h>
#include"wtypes.h"



void GetDesktopResolution(int& width, int& height)
{
    RECT desktop;
    const HWND hDesktop = GetDesktopWindow();

    GetWindowRect(hDesktop, &desktop);

    width = desktop.right;
    height = desktop.bottom;
}

int main()
{
    int colorToBe = 5287756;
    int width = 0;
    int height = 0;
    GetDesktopResolution(width, height);
    int p1[] = { width * 0.4453125 , height * 0.53125 };
    int p2[] = { width * 0.5546875 , height * 0.53125 };
    int p3[] = { width * 0.4453125 , height * 0.5972222 };
    int p4[] = { width * 0.5546875 , height * 0.5972222 };

    int pointToClick[] = { ((p2[0] - p1[0]) / 2.0) + p1[0], ((p3[1] - p1[1]) / 2.0) + p1[1] };

    
    HDC dc = GetDC(NULL);
    int color = GetPixel(dc, p1[0], p1[1]);



    while (true)
    {
        HDC dc = GetDC(NULL);
        int colorArray[] = { GetPixel(dc, p1[0], p1[1]),GetPixel(dc, p2[0], p2[1]), GetPixel(dc, p3[0], p3[1]),GetPixel(dc, p4[0], p4[1]) };

        SHORT keyState = GetKeyState('Q');
        bool isToggled = keyState & 1;
        bool isDown = keyState & 0x8000;

        if (colorArray[0] == colorToBe && colorArray[1] == colorToBe && colorArray[2] == colorToBe && colorArray[3] == colorToBe) {
            SetCursorPos(pointToClick[0], pointToClick[1]);
            mouse_event(MOUSEEVENTF_LEFTDOWN, pointToClick[0], pointToClick[1], 0, 0);
            mouse_event(MOUSEEVENTF_LEFTUP, pointToClick[0], pointToClick[1], 0, 0);
        }
        if (isToggled || isDown)
            exit(1);
    }
    return 0;
   
}