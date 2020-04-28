class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(-1, len(nestedList) * -1 - 1, -1):
            print "original ", nestedList[i]
            self.stack.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack[-1]
        # print "cur ", cur

        # handle integer
        if cur.isInteger():
            return self.stack.pop().getInteger()

        while len(self.stack) != 0 and not self.stack[-1].isInteger():
            cur = self.stack.pop()
            curList = cur.getList()
            for i in range(-1, len(curList) * -1 - 1, -1):
                print "inside ", curList[i]
                self.stack.append(curList[i])

        # print "next : ", self.stack[-1].getInteger()
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """

        while len(self.stack) != 0 and not self.stack[-1].isInteger():
            cur = self.stack.pop()
            curList = cur.getList()
            for i in range(-1, len(curList) * -1 - 1, -1):
                print "inside ", curList[i]
                self.stack.append(curList[i])

        return len(self.stack) > 0