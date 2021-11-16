for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    for i in range(1, n):
        m = max(m, a[i]-a[i-1])
    print(m)
