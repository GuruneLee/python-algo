# 토마토
import math
from collections import deque

m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ccc = 0
pos = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            pos.append([i, j])
        if l[i][j] == 0:
            ccc += 1

q = deque([p for p in pos])

if len(q) == n*m or ccc == 0:
    print(0)
    exit(0)


def bfs(l):
    while q:
        cpos = q.popleft()
        cval = l[cpos[0]][cpos[1]]
        for i in range(4):
            npos = [cpos[0]+dx[i], cpos[1]+dy[i]]
            if npos[0] < 0 or npos[0] > n-1 or npos[1] < 0 or npos[1] > m-1:
                continue
            nval = l[npos[0]][npos[1]]
            if nval != 0:
                continue
            l[npos[0]][npos[1]] = cval+1
            q.append(npos)


def isFin(l):
    for i in range(n):
        for j in range(m):
            if l[i][j] == 0:
                return False
    return True


bfs(l)
if not isFin(l):
    print(-1)
else:
    print(max(map(max, l))-1)
