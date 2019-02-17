import pyautogui as pyg
import keyboard
from PIL import Image
import numpy
import fixedQueue
import datetime
import glob
import time

screenWidth, screenHeight = pyg.size()
pyg.PAUSE = 0.001

moveDuration = 0.01

'''def blackWhitePainter():
    #black and white version
    for i, line in enumerate(arr):
        for j, pixel in enumerate(line):
            if(keyboard.is_pressed("esc")):
                break
            if pixel:
                pyg.moveTo(xStart+j, yStart+i)
                pyg.click()
                #print("column", i, "row", j)
    #pic.show()'''

#help(pyautogui)
colourStore = fixedQueue.fixQueue()

def storeChange(red, green, blue):
    location = colourStore.location((red, green,blue))
    pyg.moveTo(location[0], location[1], duration = moveDuration)
    pyg.click()
    timeSaved.add()

def changeToColour(red, green, blue):
    if colourStore.contains((red,green,blue)):
        storeChange(red, green, blue)
        return

    LOCATIONS = [(880, 455, str(red)),
     (880, 477, str(green)),(880,500, str(blue))]
    otherDuration = 0.15
    pyg.moveTo(990, 70, duration=moveDuration)#edit colour
    pyg.click()
    for item in LOCATIONS:
        if(keyboard.is_pressed("esc")):
            break
        if item[1] == 455:
            pyg.moveTo(item[0], item[1], duration=otherDuration)
            pyg.doubleClick()
        else:
            pyg.press("tab")
        pyg.typewrite(item[2])
    pyg.press("enter")
    time.sleep(0.1)
    colourStore.add((red, green, blue))

def colourPaint(xStart, yStart, arr):
    for i, line in enumerate(arr):
        for j, pixel in enumerate(line):
            if(keyboard.is_pressed("esc")):
                break
            changeToColour(pixel[0], pixel[1], pixel[2])
            pyg.moveTo(xStart+j, yStart+i)
            pyg.click()

def resizeMax(image, maxSize):
    width, height = image.size
    while width > maxSize or height > maxSize:
        image = image.resize((int(width//2), int(height//2)))
        width, height = image.size
    return image

"""keyboard.wait('left ctrl+0')
changeToColour(100,70,20)"""
timeSaved= fixedQueue.counter()

def getInt(question, min=None, max=None):
    question += " "
    while True:
        try:
            inpt = int(input(question))
            if min != None and inpt < min:
                raise ValueError("value too small")
            if max != None and inpt > max:
                raise ValueError("value too big")
            return inpt#return statement
        except Exception as e:
            print("{}, try again\n".format(e))


def chooseFile():
    legitFiles = glob.glob("./baseJpgs/*.jpg")
    if(len(legitFiles) == 0):
        print("you need to put a file in the baseJpgs dir")
        return None
    for i, file in enumerate(legitFiles):
        print(i, file[11:])
    fileIndex = getInt("enter index of file you want",0,len(legitFiles)-1)
    return legitFiles[fileIndex]


def getPicArr():
    pic = Image.open(chooseFile())
    pic = resizeMax(pic, getInt("what size do you want your image?"))
    arr = numpy.array(pic)
    return arr


def main():
    #look in dir with glob, give options to user, also with max size
    #pic = Image.open("./baseJpgs/mona.jpg")#old version
    arr = getPicArr()

    print(arr.shape, "\nready, press ctrl+0 to go\n")
    xlen, ylen, _ = arr.shape

    keyboard.wait('left ctrl+0')#waits till pressed before continuing

    xStart, yStart = pyg.position()
    startTime = datetime.datetime.now().time()

    colourPaint(xStart, yStart, arr)#main thing

    endTime = datetime.datetime.now().time()

    print("operation started at", startTime)
    print("operation ended at", endTime)
    print("there were {} pixels".format(xlen*ylen))
    print("you saved time with {} repeat pixels".format(timeSaved.get()))

if(__name__ == "__main__"):
    main()
