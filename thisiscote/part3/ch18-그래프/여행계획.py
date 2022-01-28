# 15:08 - 언제더라
def minus(x):
    return x-1

n, m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

plan = list(map(minus,map(int, input().split())))

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    
    if pa < pb:
        parent[b] = pa
    if pa > pb:
        parent[a] = pb


parent = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            union(parent, i, j)
            
for i in range(1, len(plan)):
    if find(parent, plan[i-1]) != find(parent, plan[i]):
        print("NO")
        exit(0)
        
print("YES")
