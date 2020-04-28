
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        stack =list()
        if len(s) == 0:
            return True

        hash = {'}': '{', ']':'[',')':'('}

        values = hash.values()
        keys = hash.keys()

        for i in s:
            if i in values:
                stack.append(i)
            if i in keys:
                if (len(stack) == 0):
                    return False
                if (stack[-1]== hash.get(i)):
                    stack.pop()
                    continue
                else:
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False



print isValid(s="{")