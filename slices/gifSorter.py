#from heapq import heappush, heappop
import os
import glob

def getAllNames():
    names = glob.glob("*.png")
    return names

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getNameVal(name):
    i = 0
    name = name.split("_")
    if len(name) > 1:
        name = name[1]
    else:
        name = name[0]
    
    while name[i] == "." or is_number(name[i]):#XXX check if good
        i+=1
    print(name, "||", name[:i])
    return name[:i]

def getFullName(base, newNum):
    if "_" in base:
        return str(newNum)+"_"+base.split("_")[1]
    else:
        return str(newNum)+"_"+base
    


def main():
    fileList = getAllNames()
    fileList.sort(key=getNameVal)
    for i, name in enumerate(fileList):
        newName = getFullName(name, i)
        print(newName)
        os.rename(name, newName)
    print("done")

if __name__ == "__main__":
    main()