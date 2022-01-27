# 20:26 20:54
import heapq as hq
INF = int(1e9)

def dijkstra(start, graph, n):
    q = []
    dist = [INF]*(n+1)
    hq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cd, cn = hq.heappop(q)
        for nn in graph[cn]:
            cost = cd + 1
            if dist[nn] > cost:
                dist[nn] = cost
                hq.heappush(q, (cost, nn))
    
    return dist

n,m = map(int,input().split())
barn = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    barn[a].append(b)
    barn[b].append(a)

start = 1
# print(barn)
tmp = dijkstra(start, barn, n)
for i in range(n+1):
    if tmp[i]==INF:
        tmp[i] = -1
MIN = max(tmp)
print(tmp.index(MIN), MIN, tmp.count(MIN))



