# 먼저 체크하고 들어가야지~

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]


def inMap(x, y):
    return 0 <= x < n and 0 <= y < m


def isSplited():
    v = [[0]*m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    c = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and l[i][j] != 0:
                c += 1
                if c == 2:
                    return True
                v[i][j] = 1
                q = deque()
                q.append([i, j])
                while q:
                    cx, cy = q.popleft()
                    for d in range(4):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        if not inMap(nx, ny):
                            continue
                        if v[nx][ny] != 0:
                            continue
                        if l[nx][ny] == 0:
                            continue
                        v[nx][ny] = 1
                        q.append([nx, ny])
    return False


def isZero():
    for i in range(n):
        for j in range(m):
            if l[i][j] != 0:
                return False
    return True


def countW(i, j):
    re = 0
    if inMap(i+1, j) and l[i+1][j] == 0:
        re += 1
    if inMap(i-1, j) and l[i-1][j] == 0:
        re += 1
    if inMap(i, j+1) and l[i][j+1] == 0:
        re += 1
    if inMap(i, j-1) and l[i][j-1] == 0:
        re += 1
    return re

# def p():
#     for i in range(n):
#         for j in range(m):
#             print(l[i][j], end=" ")
#         print()


year = 0
sp = False
z = False

while True:
    if isSplited():
        sp = True
    if isZero():
        z = True
    if sp or z:
        break

    c = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j] == 0:
                continue
            c[i][j] = countW(i, j)

    for i in range(n):
        for j in range(m):
            if l[i][j] > 0:
                tc = c[i][j]
                l[i][j] = l[i][j] - tc
                if l[i][j] < 0:
                    l[i][j] = 0
    # print()
    # p()
    # print()
    year += 1


if sp:
    print(year)
else:
    print(0)
