INF = int(1e9)

n = int(input())
m = int(input())

w = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    w[a][b] = min(w[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            w[a][b] = min(w[a][b], w[a][k]+w[k][b])
                
for i in range(1, n+1):
    for j in range(1, n+1):
        if w[i][j]==INF or i==j:
            print(0, end=" ")
        else:
            print(w[i][j], end=" ")
    print()