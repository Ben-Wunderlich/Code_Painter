import pyautogui as pyg
import keyboard
import random
from random import randint
import math
from math import sin, cos
import imageToPaint
import time


#put mouse in ms paint to make
screenWidth, screenHeight = pyg.size()
pyg.PAUSE = 0.005

def Template(n, size=40):
    xi, yi = pyg.position()
    i=0
    while True:
        if(keyboard.is_pressed("esc")):
            break

        x="xxx"
        x*=size
        y="xxx"
        y*=size
        pyg.moveTo(xi+x, yi+y, moveDuration)
        inverseClick()
        i+=1
    pyg.mouseUp()

def inverseClick(doReg=False):
    if doReg:
        pyg.click()
    else:
        pyg.mouseUp()
        pyg.mouseDown()

def constrain(value, min, max):
    assert min < max
    if value > max:
        value = value % max
        while value < min:
            value += 1
    return value

def makeRectangle(height, width):
    pyg.dragRel(width, 0, duration=moveDuration)   # move right
    pyg.dragRel(0, height, duration=moveDuration)   # move down
    pyg.dragRel(-width, 0, duration=moveDuration)  # move left
    pyg.dragRel(0, -height, duration=moveDuration)  # move up

def dualIncrease(x1, x2, rate):
    x1 += rate
    x2 += rate
    return x1,x2

def waitForRelease(*keys):
    for key in keys:
        while(keyboard.is_pressed(key)):
            time.sleep(0.1)

def makeStar(height, width):#note that up and down is dist from top left
    pyg.dragRel(width, height, duration=moveDuration)#down right
    pyg.dragRel(width, -height, duration=moveDuration)#up right
    pyg.dragRel(-width, -height, duration=moveDuration)#up left
    pyg.dragRel(-width, height, duration=moveDuration)#down left

def inscribedRectangles(height, width, decrease=8):
    while height > 1 and width > 1:
        if keyboard.is_pressed("esc"):
            break
        makeRectangle(height, width)
        height -=decrease
        width-=decrease
        pyg.moveRel(4,4)

def accidentalShape(height, width):
    while height > 4 and width > 4:
        if keyboard.is_pressed("esc"):
            break
        makeRectangle(height, width)
        height -=5
        width-=5

def makeMovingInscribedRectangles(height, width):
    while height > 2 and width > 2:
        if keyboard.is_pressed("esc"):
            break
        makeRectangle(height, width)
        height -=4
        width-=4
        pyg.moveRel(8,8)

def randomShape():
    slowerDuration = 0.4
    while True:
        if keyboard.is_pressed("esc"):
            break
        pyg.dragRel(randint(-50,50), randint(-50,50), duration=slowerDuration)

def squareSpiral(width, height, xMax=math.inf, yMax=math.inf):
    while width < xMax and height < yMax:
        if keyboard.is_pressed("esc"):
            break
        pyg.dragRel(width, 0, duration=moveDuration)# move right
        pyg.dragRel(0, height, duration=moveDuration)
        width, height = dualIncrease(width, height, 5)
        pyg.dragRel(-width, 0, duration=moveDuration)
        pyg.dragRel(0, -height, duration=moveDuration)
        width, height = dualIncrease(width, height, 5)

def makeSomething(height):
    i=0
    while True:
        if(keyboard.is_pressed("esc")):
            break
        """pyg.dragRel(math.ceil(math.sin(i)*height),
        math.ceil(math.cos(i)*height), duration=moveDuration)"""
        pyg.dragRel(math.ceil(math.cos(i)*height),
        math.ceil(math.sin(i)*height), duration=moveDuration)
        i+=1
        height += 1

def makeSinWave(amplitude):
    xCord, yCord = pyg.position()
    i = 0
    while i < math.pi*4:
        if(keyboard.is_pressed("esc")):
            break
        xMod = int(round(i*amplitude,0))
        yMod = int(round(math.cos(i)*amplitude, 0))
        pyg.moveTo(xCord+xMod, yCord+yMod, duration=moveDuration)
        inverseClick()
        i+= circleDetail

def makeCircle(radius):
    i = -math.pi
    xCord, yCord = pyg.position()
    xCord += radius
    while i < math.pi:
        if(keyboard.is_pressed("esc")):
            break
        xMod = int(round(math.cos(i)*radius, 0))
        yMod = int(round(math.sin(i)*radius, 0))
        pyg.moveTo(xCord+xMod, yCord+yMod, duration=moveDuration)
        inverseClick()
        i+= circleDetail
    pyg.mouseUp()

def inscribedCircles(radius, increaseRate = 2):
    while radius > 2:
        if(keyboard.is_pressed("esc")):
            break
        makeCircle(radius)
        radius -= increaseRate*2
        pyg.moveRel(increaseRate+2, 0)

def makeTriangle(sideLength):
    for _ in range(sideLength):
        pyg.dragRel(1, 1, duration=moveDuration)
    for _ in range(sideLength*2):
        pyg.dragRel(-1, 0, duration=moveDuration)
    for _ in range(sideLength):
        pyg.dragRel(1, -1, duration=moveDuration)


def funkyInscribeTriangles(sideLength, increaseRate = 6):
    while sideLength > 2:
        if(keyboard.is_pressed("esc")):
            break
        makeTriangle(sideLength)
        sideLength -= increaseRate
        pyg.moveRel(0, increaseRate//2 + 5)

def regInscribeTriangle(sideLength, increaseRate = 20):
    while sideLength > 2:
        if(keyboard.is_pressed("esc")):
            break
        makeTriangle(sideLength)
        sideLength -= increaseRate
        pyg.moveRel(0, increaseRate//2 + 2)

#failed
def sierpinki(sideLength):
    used = False
    if(sideLength <= 10):
        return

    for i in range(sideLength):
        pyg.dragRel(1, 1, duration=moveDuration)
        if(i+sideLength)/2 < i and not used:
            sierpinki(sideLength//2)
            used = True
    for i in range(sideLength*2):
        pyg.dragRel(-1, 0, duration=moveDuration)
    for i in range(sideLength):
        if(i+sideLength)/2 < i and not used:
            sierpinki(sideLength//2)
            used = True
        pyg.dragRel(1, -1, duration=moveDuration)

def goldenRatio():
    print("placeholder")
    #use to make a spiral such that ratio of positions is gold

def trueSpiral(radius, maxRadius=math.inf):
    i = -math.pi
    xCord, yCord = pyg.position()
    xCord += radius
    while radius < maxRadius:
        if(keyboard.is_pressed("esc")):
            break
        xMod = int(round(math.cos(i)*radius, 0))
        yMod = int(round(math.sin(i)*radius, 0))
        pyg.moveTo(xCord+xMod, yCord+yMod, duration=moveDuration)
        inverseClick()
        i+= 0.05
        radius += 0.06
    pyg.mouseUp()

def randshape(num, width):
    if(num == 0):
        makeRectangle(width, width * randint(1,3))
    elif(num == 1):
        inscribedRectangles(width, width * randint(1,3))
    elif(num == 2):
        makeSinWave(width)
    elif num == 3:
        makeSomething(int(width//2))
    elif num == 4:
        makeCircle(width)
    elif num == 5:
        trueSpiral(int(width//4))
    else:
        print("you messed up")

def liamsMess():
    while True:
        if keyboard.is_pressed("esc"):
            break
        leInt = randint(0, 5)
        width = randint(40, 60)
        randshape(leInt, width)
        waitForRelease("esc")
        pyg.moveRel(randint(-20,0),randint(-20,0))


def starSpiral(width, height, xMax=math.inf, yMax=math.inf):
    increaseRate = 5
    while width < xMax and height < yMax:
        if(keyboard.is_pressed("esc")):
            return width, height
        pyg.dragRel(width/2, height/2, duration=moveDuration)
        width += increaseRate
        pyg.dragRel(width/2, -height/2, duration=moveDuration)
        height += increaseRate
        pyg.dragRel(-width/2, -height/2, duration=moveDuration)
        width += increaseRate
        pyg.dragRel(-width/2, height/2, duration=moveDuration)
        height += increaseRate

def multiSpiral(width, height):
    #RATIO = 0.49 #for being contained
    RATIO = 0.6#for being bigger
    xCord, yCord = pyg.position()
    newWidth, newHeight = starSpiral(width, height)
    #imageToPaint.changeToColour(255,255,255)
    pyg.moveTo(xCord, yCord, duration = moveDuration)
    while(keyboard.is_pressed("esc")):
        time.sleep(0.25)
    squareSpiral(width, height, int(newWidth*RATIO), int(newHeight*RATIO))

def venDiamondgram(diamonds=3, width=None, height=None, xMult=1, yMult=0):
    LENGTH = 2
    xStart, yStart = pyg.position()
    if width == None:
        newWidth, newHeight = starSpiral(LENGTH,LENGTH)
    else:
        starSpiral(LENGTH, LENGTH, width, height)
        newWidth, newHeight = width, height
    xEnd, yEnd = pyg.position()
    waitForRelease("esc")
    for _ in range(diamonds-1):
        width = xStart - xEnd
        pyg.moveRel(width, 0, duration=moveDuration)#to center
        pyg.moveRel(width*xMult, width*yMult, duration=moveDuration)#to next center

        xStart, yStart = pyg.position()
        starSpiral(LENGTH, LENGTH, newWidth, newHeight)
        xEnd, yEnd = pyg.position()
    return newWidth, newHeight

def squareVenDiamondgram(sideLength=3, width=None, height=None):
    directions = [(1,0),(0,-1),(-1,0),(0,1)]
    for dir in directions:
        if(keyboard.is_pressed("esc")):
            break
        if(width == None):
            width, height = venDiamondgram(sideLength)
            pyg.moveRel(width, 0, duration=moveDuration)#to center
        else:
            if dir[0] == 0:
                venDiamondgram(sideLength+1, width, height, dir[0], dir[1])
            else:
                venDiamondgram(sideLength, width, height, dir[0], dir[1])

def triCircle(radius):
    makeCircle(radius)
    pyg.moveRel(radius*2, 0, moveDuration)
    makeCircle(radius)
    pyg.moveRel(-radius, radius*(1.73))
    makeCircle(radius)

def circleZag(radius):
    moveOn = False
    factor = 20
    minRad = 5
    while True:
        if(keyboard.is_pressed("esc")):
            break
        if radius < minRad:
            break
        makeCircle(radius)
        if moveOn:
            pyg.moveRel(radius*2, 0, moveDuration)
        moveOn = not moveOn
        radius -= factor  

def circleAlternate(radius):
    onLeft = True
    factor = 10
    minRad = 5
    while True:
        if(keyboard.is_pressed("esc")):
            break
        if radius < minRad:
            break
        makeCircle(radius)
        if onLeft:
            pyg.moveRel(factor*2, 0, moveDuration)
        else:
            pass#pyg.moveRel(-radius*2, 0, moveDuration)
        onLeft = not onLeft
        radius -= factor #try making it division instead #also w small num

def circleFourAlt(radius):
    count = 0
    factor = 10
    minRad = 5
    while True:
        if(keyboard.is_pressed("esc")):
            break
        if radius < minRad:
            break
        makeCircle(radius)
        if count == 0:#top
            pyg.moveRel(factor, -factor, moveDuration)
        if count == 1:#right
            pyg.moveRel(factor*2, 0, moveDuration)
        if count == 2:#bottom
            pyg.moveRel(factor, factor, moveDuration)
        if count == 3:#left
            pass
        count = (count+1)%4
        radius -= factor #try making it division instead #also w small num

def getStarHoriz(length):
    mysteryNumber = 1.5
    a = (length**2) / 2
    return (math.sqrt(a))*mysteryNumber

def inscribeStar(length, decrease=6):
    minLen = 1
    while length > minLen:
        if(keyboard.is_pressed("esc")):
            break
        makeStar(length, length)
        length-=decrease
        pyg.moveRel(getStarHoriz(decrease), 0, moveDuration)

def inscribeGrid(length):
    decrease = 6

    while length >= 1:
        makeStar(length, length)
        makeRectangle(length, length)
        length -= decrease

def aboutSame(x1, x2, y1, y2):
    threshHold = 3
    xClose = math.fabs(x1-x2)< threshHold
    yClose = math.fabs(y1-y2)< threshHold
    return xClose and yClose

def makeFlower(k, amplitude=100):
    print("k value is ", k)
    initialGot = False
    startx, starty = 0,math.inf
    xi, yi = pyg.position()
    i = 0
    final = math.pi*20 #sometimes not enough

    xf, yf = 0, 0# just initializing
    #while i < final:
    while i<1 or not aboutSame(startx, xf, starty, yf):
        if keyboard.is_pressed("esc") or keyboard.is_pressed("space"):
            break
        xf = (math.cos(k*i)*math.cos(i))*amplitude + xi
        yf = (math.cos(k*i)*math.sin(i))*amplitude + yi
        if(not initialGot):
            startx, starty = xf, yf
            initialGot = True
        pyg.moveTo(xf, yf, moveDuration)
        inverseClick()
        i += circleDetail
    print("ended at value", i)
    pyg.mouseUp()
    return (xi, yi)


def brockleyFlower():#is random
    while True:
        if(keyboard.is_pressed("esc")):
            break
        amp = randint(20, 200)
        kVal = randint(1, 15) / randint(1, 15)
        startPos = makeFlower(kVal, amp)
        pyg.moveTo(startPos[0], startPos[1], moveDuration)#also cool to leave this off

def rangeScale(val, Tmin, Tmax, Rmin, Rmax):
    res = (val-Rmin)/(Rmax-Rmin)
    res = (res*(Tmax-Tmin)) + Tmin
    #print("scaled to be", res)
    return res

def lissajous(a, b, amplitude=100):
    xi, yi = pyg.position()
    i = 0
    max = 2*math.pi
    while i < max:
        if(keyboard.is_pressed("esc")):
            break
        x = amplitude*math.sin(i*a)
        y = amplitude*math.sin(i*b)
        pyg.moveTo(xi+x, yi+y, moveDuration)
        inverseClick()
        i += circleDetail
    pyg.mouseUp()
    print("a={}, b={}".format(a, b))

def randLissajous(amp=None):
    if amp is None:
        amp = randint(50, 200)
    lissajous(randint(1,60), randint(1,60), amp)

def hypotrochoid(smallR, bigR, d, size=10):
    xi, yi = pyg.position()
    i = 0
    max = 10*math.pi
    while True:
        if(keyboard.is_pressed("esc")):
            break
        x=(bigR-smallR)*cos(i)+d*cos(((bigR-smallR)/smallR)*i)
        x*=size
        y =(bigR-smallR)*sin(i)-d*sin(((bigR-smallR)/smallR)*i)
        y*=size
        pyg.moveTo(xi+x, yi+y, moveDuration)
        inverseClick()
        i+=circleDetail
    pyg.mouseUp()
    print("smallR={}, bigR={}, d={}".format(smallR, bigR, d))

def randHypo(size=None):
    if(size is None):
        size=randint(10, 100)
    smallR = random.random()
    bigR = random.random()
    d = random.random()
    hypotrochoid(smallR, bigR, d, size)

def funFlower(d=None, repetitions=5, size=40):
    incr = 30
    if d is None:
        d = randint(2, 20)

    for i in range(2, 2+(2*repetitions), 2):
        if(keyboard.is_pressed("esc")):
            break
        startPos = makeFlower(d, size)
        pyg.moveTo(startPos[0], startPos[1], moveDuration)
        size += incr

def maurer(n, d, size=80):
    xi, yi = pyg.position()
    x=r=t=theta=0
    while True:
        if(keyboard.is_pressed("esc")):
            break
        theta += d
        if theta >=360:
            theta %=360
            pyg.mouseUp()
        aux = (n*theta)%360
        x = (aux*math.pi)/180
        r = math.sin(x)*size*2#just makes it look better
        t = ((theta*math.pi)/180)*size

        pyg.moveTo(xi+r, yi+t)
        inverseClick()
    pyg.mouseUp()
    print("used {} and {}".format(n,d))


def horlageMaurer(n, d, size=40):
    xi, yi = pyg.position()
    i=0
    theta = d
    while True:
        if(keyboard.is_pressed("esc")):
            break
        theta += 1
        x=sin(theta*n*d)
        y=cos(d*theta)
        x*=size
        y*=size
        pyg.moveTo(xi+x, yi+y)
        inverseClick()
        i+=circleDetail
    pyg.mouseUp()
    print("n = {}, d = {}, ended on {}".format(n,d, theta))

def heart(n, size=40):
    xi, yi = pyg.position()
    i=0
    while True:
        if(keyboard.is_pressed("esc")):
            break

        x=16*(sin(sin(sin(i/n))))
        x*=size*2
        y=13*cos(i*n)-5*cos(2*i/n)-2*cos(3*i*n)-cos(i*4/n)
        y*=size
        pyg.moveTo(xi+x, yi+y, moveDuration)
        inverseClick()
        i+=1
    pyg.mouseUp()


moveDuration = 0.01
circleDetail = 0.09 #smaller is more detail

def main():
    print("ready, press ctrl+0 to continue")
    keyboard.wait('left ctrl+0')#waits till pressed before continuing

    #makeRectangle(200, 200)
    #makeStar(300, 300)
    #inscribedRectangles(300, 310)
    #makeMovingInscribedRectangles(200, 180)
    #accidentalShape(200,221)
    #randomShape()#you need to keep an eye on this one
    #squareSpiral(200, 300)
    #makeSinWave(80)
    #makeSomething(20) #spiral with flat edges
    #makeCircle(200)
    #inscribedCircles(120)
    #makeTriangle(80)
    #regInscribeTriangle(200)
    #goldenRatio()
    #funkyInscribeTriangles(50)
    #trueSpiral(2)
    #liamsMess()
    #starSpiral(4, 5)
    #multiSpiral(4,5)
    #venDiamondgram(4)
    #squareVenDiamondgram(5)
    #triCircle(80)
    #circleZag(150)#start big
    #circleAlternate(126)
    #circleFourAlt(225)
    #inscribeStar(200)
    #inscribeGrid(100)#still needs work
    #makeFlower(0.9333333333333333, 200)#this one is cool!
    #brockleyFlower()
    #makeFlower(0.7333333333333333, 200)
    #lissajous(52, 55, 200)  #also very fun
    #randLissajous(200)
    #hypotrochoid(14,22,47, 1)
    #randHypo(200)    #fun
    #makeFlower(random.random(), 200)
    #funFlower(.272727, 4)#XXX
    #maurer(7, 139)#start high, is cool, likes primes
    #maurer(randint(4, 20), randint(20, 200))
    #maurer(6, 71)
    #horlageMaurer(2,39, 200)
    #horlageMaurer(402,284,220)
    #horlageMaurer(randint(1,1000), randint(1,1000),200)
    #horlageMaurer(5,105, 200)
    #heart(20,10)

if __name__ == "__main__":
    main()




'''pyautogui.click()'''
