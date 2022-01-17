import itertools

def cal(t, mtx):
    s = list(t)
    re = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            re += (mtx[s[j]][s[i]]+mtx[s[i]][s[j]])
    return re

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
all = set([i for i in range(n)])
mina = int(1e9)
for e in itertools.combinations(all, n//2):
    st = set(e)
    lk = all.difference(st)
    mina = min(mina, abs(cal(st,l)-cal(lk,l)))
print(mina)