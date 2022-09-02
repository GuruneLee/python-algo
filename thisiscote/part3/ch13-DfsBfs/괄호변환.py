def reverse(s):
    re = ""
    for c in s:
        re += "(" if c==")" else ")"
    return re

def isBalanced(s):
    n = 0
    for c in s:
        if c=='(':
            n += 1
        else:
            n -= 1
    return n==0

def isRight(s):
    n = 0
    for c in s:
        if c=='(':
            n += 1
        else:
            n -= 1
        if n<0:
            return False
    return n==0

def do(p):
    if len(p)==0: 
        return p
    
    u = ""
    v = ""
    idx = 0
    while idx!=len(p):
        u = p[:idx+1]
        v = p[idx+1:]
        if isBalanced(u) and isBalanced(v):
            break
        idx += 1
    
    if isRight(u):
        return u + do(v)
    
    re = "("
    re += do(v)
    re += ")"
    re += reverse(u[1:-1])

    return re

def solution(p):
    return do(p)

s = input()
print(solution(s))