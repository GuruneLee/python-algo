t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

d = [0, 1, 2, 4]


def f(n):
    for i in range(4, n+1):
        d.append(d[i-1] + d[i-2] + d[i-3])


f(max(n))

for i in n:
    print(d[i])
