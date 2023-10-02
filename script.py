"""
Gayathri Padmanabhan - Python script to move mouse
"""

import pyautogui as screen
import random
import time


x,y=screen.size()

print(x,y)

while True:
    x1=random.randint(0,x)
    y1= random.randint(0,y)

    screen.moveTo(x1,y1)
    time.sleep(9)


