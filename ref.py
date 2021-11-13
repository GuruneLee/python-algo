from queue import PriorityQueue
import heapq
from collections import deque
from queue import Queue
import sys
input = sys.stdin.readline

l = list(map(str, input().split()))  # list
s = input().rstrip()  # string

# iterate

# list
l = [1, 2, 3]
while l:
    print(l.pop())

# map(전사함수, 리스트)


def t(s):
    int(s)


m = map(t, l)

# lamda
l = list(map(lambda x: x+1, l))

#배열선언 - stack
l = []
l.append(1)
l.pop()  # 인덱싱 가능

# 길이 5x5 선언/입력
n, m = map(int, input().split())
ll = []
for _ in range(n):  # n은 row 개수
    ll.append(list(map(int, input().split())))
ll = []
ll = [list(map(int, input().split())) for _ in range(n)]

g = [[0] * m for _ in range(n)]

# queue
que = Queue()
que.put(3)
que.get()

# list.sort
l = [3, 5, 1, 2, 1]
l.sort()
l.sort(reverse=True)
p = sorted(l)

l2 = [[1, 2, 3], [3, 2, 1]]
l2.sort(key=lambda x: (x[1], x[0]))  # 두번째요소 먼저 / 첫번째요소 다음 기준

# dequeue
deq = deque()
deq.popleft()
deq.pop()
deq.appendleft()
deq.append()
deq.rotate(1)  # 인덱스 큰 쪽으로 한 칸 밀기
deq[1]  # deq 인덱싱

# heap
l = [1, 3, 5, 2, 4, 9, 8]
heapq.heapify(l)
heapq.heappop(l)
heapq.heqppush(l, 10)

# priority queue
que = PriorityQueue()
que = PriorityQueue(maxsize=8)
que.put(1)
que.put(2)
que.put(3)
print(que.get())
print(que.get())
print(que.get())

# ord - 문자의 유니코드 값을 돌려줌
# 유니코드를 문자로 바꾸려면 chr
print(ord('a'), ord('z')) ## 97 - 122
print(ord('A'), ord('Z')) ## 65 - 90