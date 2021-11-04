from queue import Queue

m = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        if m[i][j] == 0:
            m[i][j] = 9
            break


def getN(m):
    re = ""
    for i in range(3):
        for j in range(3):
            re += str(m[i][j])
    return re


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if getN(m) == "123456789":
    print(0)
    exit(0)

q = Queue()
q.put(getN(m))
v = {getN(m): 0}
while not q.empty():
    cs = q.get()
    cb = 0
    while True:
        if cs[cb] == '9':
            break
        cb += 1
    cx = cb // 3
    cy = cb % 3

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx > 2 or ny < 0 or ny > 2:
            continue
        ns = ""
        for b in range(9):
            if b == cb:
                ns += cs[nx*3+ny]
            elif b == nx*3+ny:
                ns += '9'
            else:
                ns += cs[b]
        if ns in v:
            continue
        if ns == "123456789":
            print(v[cs]+1)
            exit(0)
        q.put(ns)
        v[ns] = v[cs]+1
print(-1)
