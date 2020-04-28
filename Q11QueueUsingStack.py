class Queue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()
        self.count = 0

    def add(self, x):

        while(len(self.s1) != 0):
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s2.append(x)
        self.count = self.count+1

        while(len(self.s2) != 0):
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def poll(self):

        if len(self.s1) == 0:
            return "Queue Empty"

        item = self.s1.pop()
        self.count = self.count - 1
        return item

    def getCount(self):
        return self.count


Q = Queue()
Q.add(1)
Q.add(2)

print Q.poll()
Q.add(4)
Q.add(67)

print Q.getCount()