import heapq
# 내 풀이
# 모든 노드에서 dijkstra 를 한 번씩 돌려서
# i에서 j까지 가는 최단 거리를 d[i][j] 에 저장


def dijkstra(start, path, d):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if d[start][now] < dist:
            continue
        for i in path[now]:
            cost = dist + i[1]
            if cost < d[start][i[0]]:
                d[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def sol_1():
    n, m, x = list(map(int, input().split()))
    path = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, t = list(map(int, input().split()))
        path[a].append((b, t))

    d = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dijkstra(i, path, d)

    max_ = -1
    for i in range(1, n+1):
        if i != x:
            max_ = max(max_, d[x][i]+d[i][x])

    return max_

# 빠른 풀이
# 모든 노드에서 dijkstra 를 돌릴 필요 없음
# 우린 x to all, all to x 최단 거리만 구하면 됨
# x_to_all: 그래프에서 시작노드를 x로 하여 dijkstra 돌리면 됨
# all_to_x: *그래프에서 모든 엣지 방향을 반대로 하여 x시작점으로 dijkstra 돌리면 됨*


def sol_2():
    n, m, x = list(map(int, input().split()))
    path = [[] for _ in range(n+1)]
    path_reverse = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, t = list(map(int, input().split()))
        path[a].append((b, t))
        path_reverse[a].append((b, t))

    dijkstra(x, path)
    dijkstra(x, path_reverse)

    # 생략
