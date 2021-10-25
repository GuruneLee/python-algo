# 가운데를 말해요 - 다시풀기
# 자료구조 문제
# minHeap 과 maxHeap 두 개를 모두 써야 함

import sys
import heapq
input = sys.stdin.readline


n = int(input())
l = []
re = None
for i in range(n):
    cn = int(input())
    l.append(cn)
    h = l[:]
    heapq.heapify(h)

    for _ in range(i//2+1):
        re = heapq.heappop(h)
    print(re)
    n -= 1
