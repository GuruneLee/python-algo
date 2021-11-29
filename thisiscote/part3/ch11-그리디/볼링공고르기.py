n, m = map(int,input().split())
l = list(map(int, input().split()))

cb = [[-1]*3 for _ in range(n+1)]
def comb(x, r):
    if x == r:
        return 1
    if r == 1:
        return x
    if cb[x][r] == -1:
        cb[x][r] = comb(x-1, r-1) + comb(x-1, r)
    return cb[x][r]

dir = {}
for e in l:
    if e not in dir:
        dir[e] = 1
    else:
        dir[e] += 1

dis = 0
for e in dir:
    if dir[e] > 1:
        dis += comb(dir[e],2)

print(comb(n,2)-dis)