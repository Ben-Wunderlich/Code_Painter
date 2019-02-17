import pyautogui

screenWidth, screenHeight = pyautogui.size()
pyautogui.PAUSE = .01


while True:
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
