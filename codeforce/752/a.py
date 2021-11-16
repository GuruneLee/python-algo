t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    re = 0
    for i in range(len(a)):
        re = max(re, a[i]-i-1)
    print(re)
