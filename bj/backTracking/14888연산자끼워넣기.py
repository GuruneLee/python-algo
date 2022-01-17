import itertools

def cal(n, o):
    re = n[0]
    for i in range(len(o)):
        if o[i]==0:
            re += n[i+1]
        elif o[i]==1:
            re -= n[i+1]
        elif o[i]==2:
            re *= n[i+1]
        elif o[i]==3:
            if re<0:
                re = (-re)//n[i+1]
                re = -re
            else:
                re //= n[i+1]
    return re

n = int(input())
num = list(map(int, input().split()))

nop = list(map(int, input().split()))
op = [] #0+ 1- 2* 3/
for i in range(4):
    for v in range(nop[i]):
        op.append(i)

min_ = int(1e9)
max_ = -min_
for e in set(itertools.permutations(op)):
    tmp = cal(num,e)
    min_ = min(min_, tmp)
    max_ = max(max_, tmp)
print(max_)
print(min_)