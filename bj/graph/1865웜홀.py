INF = int(1e9)

def bf(n, start):
    dist = [INF] * (n+1)
    dist[start] = 0
    for _ in range(1, n):
        for edge in edges:
            s, e, t = edge
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
    for edge in edges:
        s, e, t = edge
        if dist[e] > dist[s] + t:
            return True
    return False

for _ in range(int(input())):
    n,m,w = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        s,e,t = list(map(int, input().split()))
        edges.append([s,e,t])
        edges.append([e,s,t])
    for _ in range(w):
        s,e,t = list(map(int, input().split()))
        edges.append([s,e,-t])
    
    if bf(n, 1):
        print("YES")
    else:
        print("NO")