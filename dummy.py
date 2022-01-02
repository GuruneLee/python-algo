n, m = map(int, input().split())

p = [True] * (m+1)
p[1] = False
for i in range(2, m//2+1):
    mul = 2
    while True:
        cur = mul*i
        if cur > m:
            break
        p[cur] = False
        mul += 1

for i in range(n, m+1):
    if p[i]:
        print(i)
