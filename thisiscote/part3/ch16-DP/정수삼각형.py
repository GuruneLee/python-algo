# 17:53 18:00
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        left = 0
        right = 0
        if j!=0:
            left = l[i-1][j-1]
        if j!=i:
            right = l[i-1][j]
        l[i][j] += max(left, right)

print(l)
print(max(l[n-1]))
