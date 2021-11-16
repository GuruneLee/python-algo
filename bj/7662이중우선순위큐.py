import heapq

for _ in range(int(input())):
    k = int(input())
    minh = []
    maxh = []
    inH = [False] * 1000001
    for i in range(k):
        order = input().split()
        num = int(order[1])
        if order[0] == 'I':
            heapq.heappush(minh, (num, i))
            heapq.heappush(maxh, (-num, i))
            inH[i] = True
        else:
            if len(minh) == 0:
                pass
            elif num == 1:
                while True:
                    tmp, ii = heapq.heappop(maxh)
                    if inH[ii]:
                        inH[ii] = False
                        break
            elif num == -1:
                while True:
                    tmp, ii = heapq.heappop(minh)
                    if inH[ii]:
                        inH[ii] = False
                        break
    if len(minh) == 0:
        print("EMPTY")
    else:
        m = None
        while True:
            m, ii = heapq.heappop(maxh)
            if inH[ii]:
                inH[ii] = False
                break
        M = None
        while True:
            M, ii = heapq.heappop(minh)
            if inH[ii]:
                inH[ii] = False
                break
        print(-m, M)
