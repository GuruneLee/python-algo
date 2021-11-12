from queue import PriorityQueue

vn = int(input())
t = [[] for _ in range(vn+1)]
for i in range(vn):
    s = list(map(int, input().split()))
    node = s[0]
    for j in range(1, len(s), 2):
        if s[j] == -1:
            break
        w = s[j+1]
        n = s[j]
        t[node].append([w, n])

q = PriorityQueue()
v = [-1]*(vn+1)
for i in range(1, vn+1):
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
for i in range(1, vn+1):
    if tmpV < v[i]:
        tmpV = v[i]
        tmpI = i

v = [-1]*(vn+1)
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
