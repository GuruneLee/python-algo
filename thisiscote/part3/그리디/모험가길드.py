n = int(input())
l = list(map(int, input().split()))

l.sort()

group = 0
count = 0
for i in range(len(l)):
    count += 1
    x = l[i]
    if count>=x:
        group += 1
        count = 0

print(group)
