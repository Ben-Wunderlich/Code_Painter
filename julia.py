from datetime import datetime
import numpy as np
import imageio
import keyboard
from random import randint, random
from PIL import Image
import pyautogui as pyg
from win10toast import ToastNotifier    
#import sys#add command line args if argv > 1

toaster = ToastNotifier()
dictPath = "storage\\my.secretdata"

def timeDiff(startTime, endTime):
    deltaT = endTime-startTime
    secDiff=deltaT.seconds
    if secDiff==0:
        msTime=deltaT.microseconds//1000
        ratio = str(int(msTime/1000 *100))+"% of a second"
        
        return "it took {}ms, thats {}".format(msTime,ratio)

    hDiff=0
    minDiff=0
    while secDiff >= 3600:
        secDiff-=3600
        hDiff+=1
    while secDiff >= 60:
        secDiff-=60
        minDiff+=1

    return "{}h, {}m, {}s".format(hDiff,minDiff,secDiff)


def currTime():
    a = datetime.now()
    arr = []
    arr.extend((a.hour,a.minute,a.second))
    isPm="am"
    if arr[0] > 12:
        isPm="pm"
        arr[0] -= 12
    arr = [str(el) for el in arr]
    for i in range(1,3):#1,2
        while len(arr[i]) < 2:
            arr[i]="0"+arr[i]
    return ":".join(arr)+isPm


def rangeScale(val, Tmin, Tmax, Rmin, Rmax):
    res = (val-Rmin)/(Rmax-Rmin)
    res = res*(Tmax-Tmin) + Tmin
    return res


def juliaPixel(c, x, y):
    #max=3000#for very small ones
    #max=10#too small, just inside
    max=80
    detail = 1#smaller makes it go faster, smaller is more detail
    i=0
    while i<max and x**2 + y**2 < 4:
        if(keyboard.is_pressed("esc")):
            break
        xtemp = x**2 - y**2
        y = 2*x*y  + c
        x = xtemp + c
        i+=detail
    i = int(round(rangeScale(i, 0, 255, 0, max)))
    '''if i==255:
        return(0,255,256)'''
    #return(i,i,i)#white on black
    return(0,i//1.5,i)#light blue on black
    #return(0,i,255-i)# on blue


def julia(c, width=100, height=50):
    arr = np.zeros((height, width, 3))
    #take off end bits of it so ends at minutes
    fileName = "interestingResults\\{}julia{}.png".format(randint(1,99),c)
    print("STARTING\nwidth={}\nheight={}\nc={}".format(width, height, c))
    print("operation started at", currTime())
    strtStore = datetime.now()
    print("\ncomputing {}...".format(fileName[19:-4]))

    for x in range(0, width):
        viewPort = (1.5, 1.3)#wide
        #viewPort = (0.5, 0.5)#super close
        #viewPort = (0.01, 0.01)#are you crazy?!
        #viewPort=(10,10)#super wide
        currX = rangeScale(x, -viewPort[0], viewPort[0], 0, width)
        for y in range(0, height):
            currY = rangeScale(y, -viewPort[1], viewPort[1], 0, height)
            arr[y,x]=juliaPixel(c, currX, currY)
        if keyboard.is_pressed("alt+ctrl+caps lock"):
            break

    arr = arr / arr.max() #normalizes data in range 0 - 255
    arr = 255 * arr
    img = arr.astype(np.uint8)
    imageio.imwrite(fileName, img)

    print("\n...finished!\noperation ended at", currTime())
    print("it took {}".format(timeDiff(strtStore,datetime.now())))
    toaster.show_toast("program is done","julia {}".format(c))

def main():
    #input("hit enter to start\n")
    #julia(round(random(), 3), 200, 150)
    julia(-0.55, 1000, 800)
    #julia(3,5,10)
    #julia(0.355,100,100)
    #julia(0.38,200,200)
    #julia(0.36, 1000, 1000)
    #julia(0.785, 700,500)
    #julia(0.489, 800, 500)
    #1.25 aspect ratio is good

    #things to try when have time
    #julia(0.3842, 2000, 1500)#do overnight
    #julia(0.4, 1400, 800)#also overnight, do first
    #julia(0.35, 1000, 800)#super cool

    #try negative numbers

if __name__ == "__main__":
    main()