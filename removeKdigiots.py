def removeKdigits(num, k):
    stack = list()
    if len(num) <= k:
        return "0"
    for n in num:
        print n
        if len(stack) > 0 and stack[-1] > n:
            if(k>0):
                stack.pop()
                k = k-1
        stack.append(n)
    while(k > 0):
        if stack[-1] > stack[0]:
            stack.pop()
            k = k-1
        else:
            stack = stack[k:len(stack):1]
            k=0
    return str(int("".join(stack)))

num = "2346010"
k = 2

print removeKdigits(num,k)