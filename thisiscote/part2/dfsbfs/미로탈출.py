from queue import Queue

n, m = map(int,input().split())
l = [input() for _ in range(n)]
v = [[-1] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = Queue()
q.put([0,0])
v[0][0] = 1
while not q.empty():
    cx, cy = q.get()
    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]
        if 0<=nx<n and 0<=ny<m:
            if v[nx][ny]==-1 and l[nx][ny]=='1':
                v[nx][ny] = v[cx][cy]+1
                q.put([nx,ny])
                
print(v[n-1][m-1])