import os
import time
import pyautogui

# Variables
second = 0
minute = 0
hours = 0

# Get the XY position of the mouse.
current_mouse_x, current_mouse_y = pyautogui.position()

while (True):

    # Right click the mouse.
    pyautogui.rightClick()

    print("Simple Python Autoclicker Created By Beto...")
    print('\n\n')
    print('\t\t\t\t---------- Time elapsed ----------')
    print('\t\t\t\t  %d hours: %d minutes: %d seconds' %
          (hours, minute, second))
    print('\t\t\t\t----------------------------------')
    time.sleep(1)
    second += 1
    if (second == 60):
        second = 0
        minute += 1
    if (minute == 60):
        minute = 0
        hours += 1
    os.system('cls')
