import pyautogui as pyg
import time
import keyboard
from shapeVisual import waitForRelease

screenWidth, screenHeight = pyg.size()
pyg.PAUSE = .01

print("ready, press ctrl+0 to continue")
keyboard.wait('left ctrl+0')#waits till pressed before continuing
waitForRelease("left ctrl", "0")


#for _ in range(26):
pyg.typewrite("stop breaking you fool", interval=0.01)  # type with quarter-second pause in between each key
