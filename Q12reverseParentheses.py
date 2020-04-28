class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()

        for c in s:
            if c == ")":
                string = ""
                while (stack[-1] != '('):
                    string = string + stack.pop()
                stack.pop()
                for let in string:
                    stack.append(let)
            else:
                stack.append(c)
        str1 = ""
        for ele in stack:
            str1 += ele
        return str1