#18:59 19:33

import heapq as hq
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dijkstra(start, graph, n):
    dist = [INF]*(n**2)
    start = 0*n+0
    q = []
    hq.heappush(q, (graph[0][0], start))
    dist[start] = graph[0][0]
    
    while q:
        cd, cn = hq.heappop(q)
        cx = cn//n
        cy = cn%n
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not (0<=nx<n and 0<=ny<n): continue
            nn = nx*n + ny
            nd = cd+graph[nx][ny]
            if nd < dist[nn]:
                hq.heappush(q, (nd, nn))
                dist[nn] = nd
                
    return dist[(n-1)*n + n-1]

for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    
    re = dijkstra(0, l, n)
    
    print(re)