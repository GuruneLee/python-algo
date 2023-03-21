# 치즈
## 16:13 ~ 16:50
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
ll = [list(map(int, input().split())) for _ in range(n)]

def outOfMap(i,j,n,m):
    return i<0 or j<0 or i>n-1 or j>m-1
    
def melt(n,m,ll):
    melted = set()
    cntll = [[0]*m for _ in range(n)]
    
    sx,sy = 0,0
    for i in range(n):
        flag = False
        for j in range(m):
            if ll[i][j]==0:
                sx,sy = i,j
                flag = True
                break
        if flag:
            break
                
    v = [[False]*m for _ in range(n)]
    dq = deque()
    v[sx][sy] = True
    dq.append((sx,sy))
    
    while dq:
        cx, cy = dq.popleft()
        
        for d in range(4):
            nx = cx+dx[d]
            ny = cy+dy[d]
            if outOfMap(nx,ny,n,m):
                continue
            if v[nx][ny]:
                continue
            if ll[nx][ny]==1:
                cntll[nx][ny] += 1
                if cntll[nx][ny]>=2:
                    melted.add((nx,ny))
                continue
            v[nx][ny] = True
            dq.append((nx,ny))
    
    for x,y in list(melted):
        ll[x][y] = 0
    
    # print('melted', melted)
    return len(melted)
    
numOfCheese = 0
for i in range(n):
    for j in range(m):
        if ll[i][j]==1:
            numOfCheese += 1

day = 0
while numOfCheese>0:
    numOfCheese -= melt(n,m,ll)
    day += 1
    if numOfCheese<0:
        print("EEERRRRRRRRRRRRRRRRRror")

print(day)

        
'''
0 0 1 2 3 4 5 6 7 8
0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0
2 0 0 0 2 1 0 0 0 0
3 0 0 0 1 1 1 1 0 0
4 0 0 2 1 1 1 1 0 0
5 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0
7 0 0 0 0 0 0 0 0 0
'''