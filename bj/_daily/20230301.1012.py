# 유기농 배추
## 22:45 ~ 23:17

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def outMap(a,b,n,m):
    return a<0 or a>=n or b<0 or b>=m

for _ in range(int(input())):
    m,n,k = map(int,input().split())
  
    ll = [[0]*m for _ in range(n)]
    v = [[False]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        ll[b][a] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] or ll[i][j]==0:
                continue
            
            l = deque([(i,j)])
            # print('i,j',i,j)
            cnt += 1 
            while l:
                a,b = l.popleft()
                for d in range(4):
                    na = a + dx[d]
                    nb = b + dy[d]
                    if outMap(na,nb,n,m):
                        continue
                    if ll[na][nb] == 0:
                        continue
                    if v[na][nb]:
                        continue
                    
                    v[na][nb] = True
                    l.append((na,nb))
                    
    print(cnt)
            
    



    
  