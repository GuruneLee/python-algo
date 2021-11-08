n = int(input())
l = list(map(int, input().split()))

l.sort()
sum = 0
for i in range(n):
    sum += l[i]*(n-i)
print(sum)
