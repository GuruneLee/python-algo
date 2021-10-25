# 프린터큐
from collections import deque


def isPrinted(l):
    front = l[0]
    for c in l:
        if front < c:
            return False
    return True


T = int(input())
count = 0
for _ in range(T):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    p = deque(l)
    idx = deque(i for i in range(len(l)))

    while True:
        if not isPrinted(p):
            p.rotate(-1)
            idx.rotate(-1)
            continue

        count += 1
        if idx[0] == M:
            print(count)
            count = 0
            break
        else:
            p.popleft()
            idx.popleft()
