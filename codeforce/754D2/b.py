from collections import deque
ll = []
def process(s):
    z = [] # 0 index
    o = [] # 1 index
    for i in range(len(s)):
        if s[i] == '1':
            o.append(i)
        else:
            z.append(i)
    
    z.sort(reverse=True) # zero는 뒤부터 ㅇㅇ
    
    l = []
    for i in range(min(len(z), len(o))):
        if z[i] > o[i]:
            l.append(z[i])
            l.append(o[i])
            tmp = s[z[i]]
            s[z[i]] = s[o[i]]
            s[o[i]] = tmp
        else:
            break
    l.sort()
    ll.append(l)

    return s

def isOk(s):
    for i in range(1,len(s)):
        if s[i] < s[i-1]:
            return False
    return True

for _ in range(int(input())):
    dq = deque()
    n = int(input())
    s = list(input())
    count = 0
    while True:
        if isOk(s):
            break
        count += 1
        s = process(s)   
    print(count, end='')
    for i in range(len(ll)):
        print()
        print(len(ll[i]), end = ' ')
        for e in ll[i]:
            print(e+1, end=' ')
    print()
    ll.clear()
    