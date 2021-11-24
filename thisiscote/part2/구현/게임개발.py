n, m = map(int,input().split())
a, b, d = map(int,input().split())
l = [ list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
nd = d
order = 0
l[a][b] = -1
re = 1
while True:
    order += 1
    nd = (nd+3)%4
    nx = a + dx[nd]
    ny = b + dy[nd]
    if 0<=nx<n and 0<=ny<m:
        if l[nx][ny]==1:
            l[nx][ny] = -1
            re += 1
            order = 0
            a = nx
            b = ny
        
    if order == 4:
        order = 0
        tx = nx-dx[nd]
        ty = ny-dy[nd]
        if l[tx][ty] == 0: break
        a = tx
        b = ty

print(re)