def backspaceCompare(S, T):

    if afterBackspace(S) == afterBackspace(T):
        return True
    else:
        return False

def afterBackspace(Q):
    s1 = list()
    for i in Q:
        if i == '#':
            if len(s1)!=0:
                s1.pop()
        else:
            s1.append(i)
    return s1

S = "ab##j"
T = "c#d#"
print backspaceCompare(S, T)

