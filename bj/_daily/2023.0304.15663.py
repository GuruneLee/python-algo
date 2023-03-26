# n과 m (9)
## 12:10 ~ 
import itertools as it
n,m = map(int,input().split())
l = list(map(int, input().split()))

p = sorted(list(set(it.permutations(l,m))))
for e in p:
    print(" ".join(map(str, e)))