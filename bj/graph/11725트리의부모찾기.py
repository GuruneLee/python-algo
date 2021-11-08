# pypy로 하면 시간초과
# python3로 하면 통과 하는
# 기이한 코드....

from queue import Queue
import sys
input = sys.stdin.readline

n = int(input())
t = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    t[x].append(y)
    t[y].append(x)

v = [-1]*(n+1)
q = Queue()
q.put(1)
v[1] = 0
while not q.empty():
    c = q.get()
    for i in t[c]:
        if v[i] == -1:
            v[i] = c
            q.put(i)
        
for i in range(2,n+1):
    print(v[i])
