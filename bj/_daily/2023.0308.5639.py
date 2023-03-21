# 이진 검색 트리
## 22:15 ~ 23:04
import sys
sys.setrecursionlimit(10**6)

l = []
while True:
    try:
        n = int(input())
        l.append(n)
    except:
        break

def pp(s, e):
    if s>e:
        return
    
    root = l[s]
    m = s
    for i in range(s+1, e+1):
        if l[i] < root:
            m += 1
    
    pp(s+1, m)
    pp(m+1, e)
    
    print(root)
    
pp(0, len(l)-1)