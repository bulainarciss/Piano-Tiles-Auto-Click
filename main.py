from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


#X:  558 Y:  573 RGB: (200, 101, 117)
#X:  657 Y:  573 RGB: (205, 106, 118)
#X:  726 Y:  573 RGB: (200, 102, 117)
#X:  818 Y:  576 RGB: (118,  17,   1)

def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(558, 500)[0] == 0:
        click(558, 500)
    if pyautogui.pixel(657, 500)[0] == 0:
        click(657, 500)
    if pyautogui.pixel(726, 500)[0] == 0:
        click(726, 500)
    if pyautogui.pixel(818, 500)[0] == 0:
        click(818, 500)