# 15657 n과 m - 중복조합
n, m = map(int,input().split())
l = list(map(int, input().split()))
l.sort()

def pprint(list):
    for e in list:
        print(e, end=' ')
    print()

s = []
def func(i, c):
    if c == m-1:
        pprint(s)
        return
    while i < n:
        s.append(l[i])
        func(i, c+1)
        s.pop()
        i += 1

for i in range(n):
    s.append(l[i])
    func(i,0)
    s.pop()
