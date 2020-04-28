class Solution(object):

    def custom_append(self, stack, n, k):
        while len(stack) != 0 and stack[-1] > n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

        return k

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = list()

        for n in num:
            k = self.custom_append(stack, n, k)

        for i in range(k):
            if len(stack) != 0:
                stack.pop()

        # Result stuff
        print stack, k

        if len(stack) == 0: return "0"

        # remove zeros from begining
        res = ""
        while len(stack) != 0:
            n = stack.pop()
            res = n + res

        for i in range(len(res)):
            if res[i] != "0":
                break
        return res[i:]