class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        numFlag = False
        num = ""

        for c in s:
            if c == "]":
                string = ""
                while (stack[-1] != "["):
                    string = stack.pop() + string

                stack.pop()

                value = int(stack.pop())
                res = ""
                while (value > 0):
                    res += string
                    value = value - 1
                stack.append(res)

            elif c >= "0" and c <= "9":
                num = num + c
                numFlag = True

            elif c == "[":
                if (numFlag == True):
                    stack.append(num)
                    num = ""
                    numFlag = False
                stack.append(c)

            else:
                stack.append(c)
        string = ""
        while (stack):
            string = stack.pop() + string

        return string