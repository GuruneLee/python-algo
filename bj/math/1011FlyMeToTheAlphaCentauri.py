import queue
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    t = int((y-x)**0.5)
    r = y-x-t**2
    re = 2*t - 1
    if r == 0:
        print(re)
        continue

    if r % t == 0:
        re += r//t
    else:
        re += r//t + 1
    print(re)
