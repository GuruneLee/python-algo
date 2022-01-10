n = int(input())
l = list(map(int, input().split()))
d = {}
t = sorted(set(l))
for i in range(len(t)):
    d[t[i]] = i
for i in range(n):
    l[i] = d[l[i]]

for k in l:
    print(k, end=" ")
print()
