n = int(input())
l = list(map(int, input().split()))
x = int(input())

# two pointer
l.sort()
i,j = 0,n-1
ans = 0
for _ in range(n-1):
    if l[i]+l[j]==x:
        ans += 1
    
    if l[i]+l[j]<=x:
        i+=1
    elif l[i]+l[j]>x:
        j-=1
print(ans)

# dictionary (counter)
import collections
counter = collections.Counter(l)
ans = sum(c*counter[x-v] for v,c in counter.items() if v+v<x)
print(ans)