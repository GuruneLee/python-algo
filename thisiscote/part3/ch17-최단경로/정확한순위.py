import heapq as hq
INF = int(1e9)

def dijkstra(start, graph, n):
    dist = [INF]*(n+1)
    q = []
    hq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cd, cn = hq.heappop(q)
        for nn in graph[cn]:
            if dist[nn] > cd+1:
                hq.heappush(q, (cd+1, nn))
                dist[nn] = cd+1
                
    return dist

    
n,m = map(int,input().split())
grade = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    grade[a].append(b)
    # grade[b].append(a)

re = [[INF]*(n+1)]
for i in range(1,n+1):
    re.append(dijkstra(i, grade, n))


count = 0
for k in range(1,n+1):
    s1, s2 = [], []
    for i in range(1, n+1):
        if re[i][k]!=INF:
            s1.append(i)
        if re[k][i]!=INF:
            s2.append(i)

    s = set(s1).union(set(s2))
    if len(s)==n:
        count += 1
        
print(count)