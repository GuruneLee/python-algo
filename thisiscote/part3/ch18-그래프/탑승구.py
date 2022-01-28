# 15:41 x 16:18
g = int(input())
p = int(input())
l = []
for i in range(p):
    l.append(int(input()))

# Sol 01
# 비행기를 순서대로 순회하며 도킹 가능한 가장 큰 gate 부터 도킹한다
# 도킹이 된 gate 를 체크하기 위해 parked 배열을 쓴다
# 만약 도킹 가능한 게이트가 없다면 break 한다
parked = [False]*(g+1)
for plane in range(p):
    gate = l[plane]
    while gate>0:
        if parked[gate]: 
            gate -= 1
            continue
        break
    
    if gate==0:
        break
    else:
        parked[gate] = True
        
print(parked.count(True))

# Sol 02
# 위 과정을 union-find 로 구현할 수 있다.
## 비행기를 순회하며 도킹할 수 있는 가장 큰 gate번호의 parent와 도킹한다
## 도킹이 된 gate는 바로 왼쪽의 gate와 union한다
## 만약 parent가 0이라면 도킹하지 않고 멈춘다.

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

parent = [i for i in range(g+1)]  
re = 0
for plane in range(p):
    forDock = find(parent, l[plane])
    if forDock==0:
        break
    union(parent, forDock, forDock-1)
    re += 1

print(re)
