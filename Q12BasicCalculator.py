class Solution(object):
    def calculate(self, s):
        res = 0
        digit = 0
        sign = +1
        stack = list()

        for char in s:
            if char >= '0' and char <= '9':
                digit = 10*digit + int(char)
            elif char in ["-", "+"]:
                res = res + sign*digit
                digit = 0
                if char == "-":
                    sign = -1
                else:
                    sign = +1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif char == ")":
                res = res + sign*digit
                res = res * stack.pop()
                res = res + stack.pop()
                digit = 0
        return res + digit*sign