# 다다익스트라..?
from queue import PriorityQueue

n = int(input())
t = [[] for _ in range(n+1)]
for i in range(n-1):
    r, c, w = map(int, input().split())
    t[r].append([w, c])
    t[c].append([w, r])

q = PriorityQueue()
v = [-1]*(n+1)
for i in range(1, n+1):
    if len(t[i]) != 0:
        q.put([0, t[i][0][1]])
        v[t[i][0][1]] = 0
        break

while not q.empty():
    cw, cn = q.get()
    cw = -cw
    for i in range(len(t[cn])):
        nn = t[cn][i][1]
        if v[nn] != -1:
            continue
        nw = cw + t[cn][i][0]
        q.put([-nw, nn])
        v[nn] = nw

tmpV = -1
tmpI = 0
for i in range(1, n+1):
    if tmpV < v[i]:
        tmpV = v[i]
        tmpI = i

v = [-1]*(n+1)
q.put([0, tmpI])
v[tmpI] = 0
while not q.empty():
    cw, cn = q.get()
    cw = -cw
    for i in range(len(t[cn])):
        nn = t[cn][i][1]
        if v[nn] != -1:
            continue
        nw = cw + t[cn][i][0]
        q.put([-nw, nn])
        v[nn] = nw

print(max(v))
