class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = list()
        score = 0

        for c in S:
            if c == '(':
                stack.append(c)
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while (stack[-1] != '('):
                        score = score + stack.pop()
                    stack.pop()
                    stack.append(2 * score)
        score = 0
        while (stack):
            score = score + stack.pop()

        return score

