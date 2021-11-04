R, C = list(map(int, input().split()))
cw = [input().rstrip() for _ in range(R)]


def getS(i, j, dir):
    tmp = ""
    if dir == "R":
        for r in range(i, R):
            if cw[r][j] == '#':
                break
            tmp += cw[r][j]
    elif dir == "C":
        for c in range(j, C):
            if cw[i][c] == '#':
                break
            tmp += cw[i][c]
    return tmp


s = []
for i in range(R):
    for j in range(C):
        tmp = ""
        if i == 0:
            tmp = getS(i, j, "R")
        elif cw[i-1][j] == '#':
            tmp = getS(i, j, "R")
        if len(tmp) > 1:
            s.append(tmp)

        tmp = ""
        if j == 0:
            tmp = getS(i, j, "C")
        elif cw[i][j-1] == '#':
            tmp = getS(i, j, "C")
        if len(tmp) > 1:
            s.append(tmp)
s.sort()
print(s[0])
