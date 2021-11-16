import heapq

n = int(input())
minh = [100001]
maxh = [0]

for i in range(n):
    if i % 2 == 0:
        heapq.heappush(maxh, -int(input()))
    else:
        heapq.heappush(minh, int(input()))

    while -maxh[0] > minh[0]:
        t1 = -heapq.heappop(maxh)
        t2 = heapq.heappop(minh)
        heapq.heappush(maxh, -t2)
        heapq.heappush(minh, t1)

    print(-maxh[0])
