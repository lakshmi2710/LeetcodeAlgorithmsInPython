class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = j = 0
        stack = list()

        while (i < len(pushed) and j < len(popped)):
            if (len(stack) > 0 and stack[-1] == popped[j]):
                stack.pop()
                j = j + 1
            elif (pushed[i] != popped[j]):
                stack.append(pushed[i])
                i = i + 1
            elif (pushed[i] == popped[j]):
                i = i + 1
                j = j + 1

        if (len(stack) > 0):
            while (j < len(popped)):
                if (stack[-1] == popped[j]):
                    stack.pop()
                    j = j + 1
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False