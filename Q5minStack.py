class MinStack():

    def __init__(self):
        self.main_stack = list()
        self.min_stack = list()

    def push(self,x):
        self.main_stack.append(x)

        if (len(self.min_stack) == 0) or (x <= self.min_stack[-1]):
            self.min_stack.append(x)
            return
        return

    def pop(self):

        if (len(self.main_stack) == 0):
            return "Stack Empty"

        item = self.main_stack.pop()
        if(self.min_stack[-1] == item):
            self.min_stack.pop()
        return

    def top(self):
        if (len(self.main_stack) == 0):
            return []
        return(self.main_stack[-1])

    def getMin(self):
        if (len(self.main_stack) == 0):
            return []
        return(self.min_stack[-1])


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print minStack.getMin()
print minStack.pop()

print minStack.getMin()