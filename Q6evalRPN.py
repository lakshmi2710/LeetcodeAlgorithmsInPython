import math

def evalRPN(tokens):
    stack = list()

    for op in tokens:

        if (op == '+' or op == '-' or op == '*' or op == '/'):
            """
            """
            sec = int(stack.pop())
            first = int(stack.pop())

            if op == "+":
                stack.append(str(first + sec))
            if op == "-":
                stack.append(str(first - sec))
            if op == "*":
                stack.append(str(first * sec))

            if op == "/" :
                res = first / sec
                print res
                if res < 0 and res * sec != first:
                    res += 1
                print res, first, sec

                stack.append(str(res))

        else:
            stack.append(op)

    return stack[-1]

Input = ["4","-2","/","2","-3","-","-"]

print evalRPN(Input)