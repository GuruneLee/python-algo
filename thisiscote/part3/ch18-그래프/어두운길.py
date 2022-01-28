# 17:58 - 18:12
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
edge = []
for i in range(m):
    a,b,cost = map(int,input().split())
    edge.append((cost, a, b))

edge.sort()

total = sum(list(map(lambda x : x[0], edge)))
parent = [i for i in range(n)]
for i in range(m):
    ccost, ca, cb = edge[i]
    if find(parent, ca) == find(parent, cb):
        continue
    total -= ccost
    union(parent, ca, cb)

print(total)
    