import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = list(map(lambda x: 10**x, l))
    idx = 0
    c = []
    flag = True
    if n == 1:
        print(k+1)
    else:
        for i in range(1, n):
            t = l[i] - l[i-1]
            need = t//l[i-1]
            if need > k:
                c.append(k)
                flag = False
                break
            k -= need
            c.append(need)
        if flag:
            c.append(k)
        c[len(c)-1] += 1
        ans = 0
        for i in range(len(c)):
            ans += c[i]*l[i]
        print(ans)
