class fixQueue:
    def __init__(self, length=10):
        self.qList = [(-1,-1,-1)]*length
        print(self.qList)

    def __str__(self):
        return str(self.qList)

    def add(self, item):
        self.qList.insert(0, item)
        self.qList = self.qList[:-1]

    def contains(self, item):
        return item in self.qList

    def location(self, item):
        if not self.contains(item):
            return None
        indx = self.qList.index(item)
        yLocation = 105
        xLocation = 960 - 22*indx
        return(xLocation, yLocation)

class counter:
    def __init__(self):
        self.count = 0
    def __str__(self):
        return str(self.count)
    def add(self):
        self.count +=1
    def get(self):
        return self.count

if __name__ == '__main__':
    qu = queue(12)
    print(qu)
    qu.add((11,2,54))
    qu.add((1,2,3))
    qu.add((2,1,3))
    print(qu)
    print(qu.contains((0,0,0)))
    print(qu.location((11,2,54)))
