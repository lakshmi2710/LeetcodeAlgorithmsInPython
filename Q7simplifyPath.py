def simplifyPath(simplifyPath):
    """

    :param simplifyPath:
    :return:
    """

    path = simplifyPath.split('/')
    stack = list()

    for ele in path:
        if ele in ('', '.'):
            pass
        elif ele == "..":
            if(len(stack) != 0):
                stack.pop()
        else:
            stack.append(ele)
    return '/'+'/'.join(stack)


path = "/../"
print simplifyPath(path)