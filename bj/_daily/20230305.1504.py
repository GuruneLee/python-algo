# 특정한 최단 경로
## 17:12 ~ 17:36, 18:47~
import heapq as hq
import sys
input=lambda:sys.stdin.readline().rstrip()

n,e = map(int,input().split())
E = {}
for i in range(1, n+1):
    E[i] = []
    
for _ in range(e):
    a,b,c = map(int,input().split())
    E[a].append((c,b))
    E[b].append((c,a))

u,v = map(int,input().split())

def dijkstra(s, E, n):
    dist = [int(1e9)]*(n+1)
    dist[s] = 0
    
    pq = []
    hq.heappush(pq, (0,s))
    while pq:
        cdist, cnode = hq.heappop(pq)
        # print(cdist, cnode)
        for d, nnode in E[cnode]:
            if d+cdist < dist[nnode]:
                dist[nnode] = d+cdist
                hq.heappush(pq,(dist[nnode],nnode))

    return dist

one = dijkstra(1,E,n)
uu = dijkstra(u,E,n)
vv = dijkstra(v,E,n)

ans = int(1e9)
# 1~u, u~v, v~n
ans = min(ans, one[u] + uu[v] + vv[n])
# 1~v, v~u, u~n
ans = min(ans, one[v] + vv[u] + uu[n])

print(ans if ans<int(1e9) else -1)