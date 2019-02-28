import datetime
import numpy as np
import imageio
import keyboard
from random import randint, random
from PIL import Image
import pyautogui as pyg
import mqueue

colourDict = {}
savedQueue = mqueue.wQueue()
tempColours = []
dictPath = "storage\\my.secretdata"
USE_STORED = True



def currTime():
    a = datetime.datetime.now().time()
    a = str(a).split(":")
    isPm="am"
    if int(a[0]) > 12:
        isPm="pm"
        a[0] = int(a[0])-12
    final = str(a[0])+":"+a[1]+isPm
    return final


def rangeScale(val, Tmin, Tmax, Rmin, Rmax):
    res = (val-Rmin)/(Rmax-Rmin)
    res = (res*(Tmax-Tmin)) + Tmin
    return res

def dictToMemory(myDict=colourDict):#make names for each one and can choose
    allItems = []
    for val in tempColours:
        bStr = ",".join([str(a) for a in val])
        allItems.append(bStr)
    with open(dictPath, "w+") as outFile:
        outFile.write("\n".join(allItems))
    print("{} colours saved".format(len(colourDict)))
    #XXX make thing to update it
 
def dictFromMemory():#remove arg, just for testing
    #global colourDict
    with open(dictPath, "r") as inFile:
        for col in inFile:
            rgb = [int(el) for el in col.split(",")]
            savedQueue.add(rgb)

def attentionWiggle():
    dur = 0.13
    wiggle=40
    goLeft = True
    pyg.moveTo(800, 400, dur)
    for _ in range(0,2):
        if goLeft:
            pyg.moveRel(wiggle,0,dur)
        else:
            pyg.moveRel(-wiggle,0,dur)
        goLeft = not goLeft


def juliaPixel(c, x, y):
    max=1000
    detail = 1#smaller makes it go faster, smaller is more detail
    i=0
    while i<max and x**2 + y**2 < 4:
        if(keyboard.is_pressed("esc")):
            break
        xtemp = x**2 - y**2
        y = 2*x*y  + c
        x = xtemp + c
        i+=detail
    i = rangeScale(i, 0, 255, 0, max)

    if i not in colourDict.keys():
        if savedQueue.isEmpty():
            colourDict[i] = (randint(0,255), randint(0,255), randint(0,255))
        else:
            colourDict[i] = savedQueue.remove()
        tempColours.append(colourDict[i])
    
    return colourDict[i]

def julia(c, width=100, height=50):
    arr = np.zeros((height, width, 3))
    startTime = currTime()
    #take off end bits of it so ends at minutes
    fileName = "interestingResults\\{}julia{}.png".format(randint(1,99),c)
    print("STARTING\nwidth={}\nheight={}\nc={}".format(width, height, c))
    print("operation started at", startTime)
    print("\ncomputing fractal...")

    for x in range(0, width):
        currX = rangeScale(x, -1.1, 1.1, 0, width)
        for y in range(0, height):
            currY = rangeScale(y, -1.4, 1.4, 0, height)
            arr[y,x]=juliaPixel(c, currX, currY)
    endTime = currTime()
    imageio.imwrite(fileName, arr)
    print("there were {} colours".format(len(colourDict)))
    print("operation ended at", endTime)
    #Img = Image.open(fileName)#replace with other thing
    #Img.show()
    attentionWiggle()

def colourChoice():
    inp = input("do you like the colour scheme?(y/n)")
    if inp == "y":
        dictToMemory(colourDict)
    else:
        print("that's too bad")

def main():
    load = bool(input("enter to start or 1 to load saved colours\n"))
    if load:
        dictFromMemory()
    #julia(round(random(), 3), 200, 150)
    #julia(0.626, 500, 500)#try with different detail levels
    julia(0.25, 150, 100)
    #julia(0.785, 700,500)
    #julia(0.489, 800, 500)
    #1.25 aspect ratio is good

    #things to try when have time
    #julia(0.3842, 2000, 1500)#do overnight
    #julia(0.4, 1400, 800)#also overnight, do first

    #try negative numbers
    if not load:
        colourChoice()
    

if __name__ == "__main__":
    main()