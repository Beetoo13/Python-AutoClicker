import os
import time
import pyautogui
import time

# Variables
clicksCounter = 1
second = 0
minute = 0
hours = 0

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()

while (True):

    # Right click the mouse.
    pyautogui.rightClick()

    clicksCounter = clicksCounter + 1

    print("Simple Python Stopwatch Created By Beto...")
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
