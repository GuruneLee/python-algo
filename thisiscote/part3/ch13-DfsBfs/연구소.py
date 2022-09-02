# 12:42 - 15:52
from copy import deepcopy
from itertools import permutations
from collections import deque

def bfs(l, vir):
    graph = deepcopy(l)
    
    q = deque()
    for v in vir:
        q.append(v)
    
    while q:
        vx, vy = q.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 2
    
    return graph

dx = [-1,1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
    
virus = [] #2
empty = [] #0

for i in range(n):
    for j in range(m):
        if l[i][j] == 2:
            virus.append((i,j))
        if l[i][j] == 0:
            empty.append((i,j))

max_ = 0
for nwalls in permutations(empty, 3):
    for nwall in nwalls:
        l[nwall[0]][nwall[1]] = 1
    expansion = bfs(l, virus)
    canSave = sum(x.count(0) for x in expansion)
    if canSave != 0:
        max_ = max(max_, canSave)
    for nwall in nwalls:
        l[nwall[0]][nwall[1]] = 0
print(max_)