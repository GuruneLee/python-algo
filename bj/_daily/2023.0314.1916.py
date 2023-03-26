# 최소비용 구하기
import sys
input=lambda:sys.stdin.readline().rstrip()

from collections import defaultdict
from heapq import heappop, heappush

n = int(input())
m = int(input())

g = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input().split())
    g[a-1].append((b-1,c))

s,b = map(int,input().split())

q = []
v = [int(1e9)]*n
v[s-1] = 0
heappush(q, (0, s-1))

while q:
    cst, nd = heappop(q)
    eset = g[nd]
    if v[nd] < cst:
        continue
    for i in range(len(eset)):
        ncst, nnd = eset[i][1], eset[i][0]
        if ncst+cst < v[nnd]:
            heappush(q, (ncst+cst, nnd))
            v[nnd] = ncst+cst
            
print(v[b-1])