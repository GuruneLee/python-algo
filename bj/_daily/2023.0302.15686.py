# 치킨 배달
## 21:58 ~ 답봄 (https://codesyun.tistory.com/185.)
import itertools as it

n,m = map(int,input().split())
ll = [list(map(int, input().split())) for _ in range(n)]

home = []
chick = []

for i in range(n):
    for j in range(n):
        if ll[i][j] == 1:
            home.append((i,j))
        elif ll[i][j] == 2:
            chick.append((i,j))

dist = [[0]*len(home) for _ in range(len(chick))]
for i in range(len(chick)):
    for j in range(len(home)):
        dist[i][j] = abs(chick[i][0]-home[j][0]) + abs(chick[i][1]-home[j][1])

re = 987654321    
for c in it.combinations(chick, m):
    tre = 0
    for h in home:
        min_ = 9876
        for j in range(m):
            min_ = min(min_, abs(h[0]-c[j][0])+abs(h[1]-c[j][1]))
        tre += min_
    re = min(tre, re)

print(re)