import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    b = 1
    sum = 1
    h = 0
    flag = False
    while True:
        if sum >= n:
            flag = True
            break

        sum += b
        h += 1

        if b*2 > k:
            b = k
            break
        else:
            b = b*2

    if not flag:
        left = n-sum
        h += left//b
        if left % b != 0:
            h += 1
    print(h)
