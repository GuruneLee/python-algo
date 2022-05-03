from collections import deque

n = int(input())

l = []
v = []
for i in range(n):
    l.append(list(map(int, input().split())))
    v.append(l[i])

q = deque()
for i in range(3):
    q.append((0, i))

while q:
    cx, cy = q.popleft()
    if cx == n-1:
        continue
    print(cx, cy, end="/")
    for dy in range(-1, 2, 1):
        ny = cy + dy
        nx = cx + 1
        if not (0 <= ny <= 2):
            continue
        print(nx, ny, end=", ")
        q.append((nx, ny))
        tmp = v[cx][cy] + l[nx][ny]
        v[nx][ny] = max(v[nx][ny], tmp)
    print()

print(v)
