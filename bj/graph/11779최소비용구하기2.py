# 11779 최소비용구하기2
import heapq
INF = int(1e9)


def trace(end, l):
    path = [end]
    cnt = 1

    idx = end
    while True:
        next = l[idx]
        if next == -1:
            break
        path.append(next)
        cnt += 1
        idx = next

    return (cnt, reversed(path))


def dijkstra(start, graph):
    distance = [INF]*len(graph)
    pre = [-1]*len(distance)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                pre[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

    return (distance, pre)


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))

a, b = map(int, input().split())
v, pre = dijkstra(a, graph)

print(v[b])
cnt, path = trace(b, pre)
print(cnt)
for e in path:
    print(e, end=" ")
print()
