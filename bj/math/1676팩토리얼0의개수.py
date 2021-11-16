import math
n = int(input())
n2 = 0
n5 = 0
for i in range(1, n+1):
    tmp = i
    while tmp % 2 == 0:
        n2 += 1
        tmp = tmp//2
    tmp = i
    while tmp % 5 == 0:
        n5 += 1
        tmp = tmp//5

print(min(n2, n5))
