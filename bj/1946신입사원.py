import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l.sort()

    count = 1  # 채용인원
    MIN = l[0][1]
    for i in range(1, n):
        if MIN > l[i][1]:
            count += 1
            MIN = l[i][1]

    print(count)
