def toJ(s):
    return s[0].upper() + s[1:].lower()        
    
def solution(s):
    j = "".join(list(map(lambda x: toJ(x) ,s.strip().split())))
    n = len(s)
    
    space = 0    
    i = 0
    ans = ""
    while i+space<n:
        if s[i+space] == " ":
            ans += " "
            space += 1
        else:
            ans += j[i]
            i += 1
    return ans