n = int(input())

d = [0, 0, 1, 3]
if n == 1 or n == 2 or n == 3:
    print(d[n])
    exit(0)
for i in range(4, n+1):
    tmp = -1
    for a in range(1, i//2):
        b = i-a
        tmp = max(tmp, d[a]+d[b]+a*b)
    d.append(tmp)

print(max(d))
