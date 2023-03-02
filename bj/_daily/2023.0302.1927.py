# 최소힙
## 20:38 ~ 20:43

import heapq as h
import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
l = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(l)==0:
            print(0)
        else:
            print(h.heappop(l))
    else:
        h.heappush(l,x)

# min heap 구현
