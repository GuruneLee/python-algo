n, m, k = map(int,input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)

c = 0
sum = 0
for _ in range(m):
    if c==k:
        c = 0
        sum += l[1]
        continue
    sum += l[0]
    c += 1
print(sum)