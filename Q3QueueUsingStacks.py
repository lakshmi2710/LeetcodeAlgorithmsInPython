class Queue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x):

        while(len(self.s1) != 0):
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s2.append(x)

        while(len(self.s2) != 0):
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def pop(self):

        if len(self.s1) == 0:
            return "Queue Empty"

        item = self.s1.pop()
        return item

    def peek(self):
        if len(self.s1) == 0:
            return "Queue Empty"
        return self.s1[-1]

    def empty(self):
        if len(self.s1) == 0:
            return True
        else:
            return False

Q = Queue()
Q.push(1)
Q.push(2)
print Q.peek()
print Q.pop()
print Q.empty()