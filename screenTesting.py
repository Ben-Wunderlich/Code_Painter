import pyautogui as pyg

while True:
    xPos = int(input("x position plz "))
    yPos = int(input("y position plz "))
    pyg.moveTo(xPos, yPos, duration=0.5)
    print("\nmoving to ({}, {})\n".format(xPos,yPos))
