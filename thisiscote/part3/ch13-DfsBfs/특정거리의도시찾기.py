# 11:47
import heapq as hq
INF = int(1e9)
n,m,k,x = map(int,input().split())
l = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    
q = []
d = [INF]*(n+1)
d[x] = 0
hq.heappush(q, (0, x))
while q:
    dist, node = hq.heappop(q)
    for v in l[node]:
        if d[v] > dist + 1:
            hq.heappush(q, (dist+1, v))
            d[v] = dist+1

ans = []
for i in range(1, n+1):
    if d[i]==k:
        ans.append(i)

if not ans:
    print(-1)
else:
    print("\n".join(map(str, sorted(ans))))