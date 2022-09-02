# 16:15
import heapq as hq
n, k = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
s, X, Y = map(int,input().split())
        
q = []
for i in range(n):
    for j in range(n):
        if l[i][j] != 0:
            hq.heappush(q, (0, l[i][j], i, j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
while q:
    t, v, x, y = hq.heappop(q)
    if t==s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<n): continue
        if l[nx][ny] != 0: continue
        hq.heappush(q, (t+1, v, nx, ny))
        l[nx][ny] = v

print(l[X-1][Y-1])