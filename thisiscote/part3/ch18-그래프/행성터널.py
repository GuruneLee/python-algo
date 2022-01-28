# 18:21 - 18:44
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
        
n = int(input())
pos = []
for i in range(n):
    x,y,z = map(int,input().split())
    pos.append((x,y,z,i))

sortedByX = sorted(pos, key=lambda x: x[0])
sortedByY = sorted(pos, key=lambda x: x[1])
sortedByZ = sorted(pos, key=lambda x: x[2])

edge = []
for i in range(1, n):
    x = sortedByX[i][0] - sortedByX[i-1][0]
    y = sortedByY[i][1] - sortedByY[i-1][1]
    z = sortedByZ[i][2] - sortedByZ[i-1][2]
    edge.append((x, sortedByX[i][3], sortedByX[i-1][3]))
    edge.append((y, sortedByY[i][3], sortedByY[i-1][3]))
    edge.append((z, sortedByZ[i][3], sortedByZ[i-1][3]))

# 여기서 edge를 정렬하지 않고 heap을 사용해도 되겠구낭
edge.sort()
re = 0
p = [i for i in range(n)]
for i in range(len(edge)):
    cost, a, b = edge[i]
    if find(p, a) == find(p, b):
        continue
    re += cost
    union(p, a, b)

print(re)