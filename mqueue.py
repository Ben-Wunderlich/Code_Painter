class wQueue:
    def __init__(self):
        self.queue = []

    def add(self, newEl):
        if newEl not in self.queue:
            self.queue.insert(0,newEl)
            return True
        return False

    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return "No elements in Queue!"
    
    def isEmpty(self):
        return len(self.queue)==0
