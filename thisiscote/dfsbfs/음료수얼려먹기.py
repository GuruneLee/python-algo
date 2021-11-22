from queue import Queue

n, m = map(int,input().split())
l = [ input() for _ in range(n)]
v = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if l[i][j] == '1':
            v[i][j] = True
count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if not v[i][j]: 
            count += 1
            q = Queue()
            q.put([i,j])
            v[i][j] = True
            while not q.empty():
                cx, cy = q.get()
                
                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if 0<=nx<n and 0<=ny<m:
                        if not v[nx][ny]:
                            v[nx][ny] = True
                            q.put([nx,ny])
                    
print(count)