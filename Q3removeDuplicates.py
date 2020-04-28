class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if (len(s) < 2 or k == 0):
            return s
        stack = list()
        stack.append(['#', 0])

        for i in s:
            if len(stack) != 0 and stack[-1][0] == i:
                stack[-1][1] = stack[-1][1] + 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i, 1])

        res = ""

        for c, i in stack:
            while (i > 0):
                res = res + c
                i = i - 1
        return res

