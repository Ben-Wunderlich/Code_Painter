import datetime
import numpy as np
import imageio
import keyboard
from random import randint, random
from PIL import Image
import pyautogui as pyg
import mqueue
import subprocess
from win10toast import ToastNotifier


toaster = ToastNotifier()
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
    a = [str(num) for num in a if len(str(num)) < 3]
    final = ":".join(a)+isPm #XXX test this
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
    with open(dictPath, "r") as inFile:
        for col in inFile:
            rgb = [int(el) for el in col.split(",")]
            savedQueue.add(rgb)

def juliaPixel(c, x, y):
    max=50
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
    fileName = "slices\\{}julia.png".format(c)
    print("operation started at", startTime)
    print("\ncomputing fractal {}...".format(fileName))

    for x in range(0, width):
        #viewPort = (1.1, 1.4)#close
        viewPort = (2.2, 2.2)#wide
        currX = rangeScale(x, -viewPort[0], viewPort[1], 0, width)
        for y in range(0, height):
            currY = rangeScale(y, -viewPort[1], viewPort[1], 0, height)
            arr[y,x]=juliaPixel(c, currX, currY)
        if(keyboard.is_pressed("esc") and keyboard.is_pressed("0")):
            return False
    endTime = currTime()
    imageio.imwrite(fileName, arr)
    print("operation ended at", endTime)
    #if savedQueue.isEmpty():#if used up all colours
    #    dictToMemory(colourDict)
    return True


def main():
    dictFromMemory()
    '''detail=0.005
    min = 0.2
    c=0.368'''
    nums = [0.381, 0.405]
    for x in nums.sort(reverse=True):
        julia(x,400,400)
    '''while c >= min:
        if not julia(c, 400, 400):
            break
        c = round(c-detail, 3)
        print("c is now", c)'''#XXVII
    toaster.show_toast("julia result","program is done")
    #subprocess.call("slices\\gifSorter.py", shell=True)

 
if __name__ == "__main__":
    main()