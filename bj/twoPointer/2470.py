n = int(input())
l = list(map(int, input().split()))
l.sort()

i,j = 0,n-1
min_s= int(2e9)
ans = (-1, -1)

for _ in range(n-1):
    s = l[i]+l[j]
    if abs(s)<min_s:
        min_s = abs(s)
        ans = (l[i], l[j])
    if l[i]+l[j]>0:
        j -= 1
    else:
        i += 1
print(ans[0], ans[1])