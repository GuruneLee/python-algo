# k! 에서 2가 총 몇개?
def two(k):
    t = 2
    re = 0
    while t<=k:
        re += k//t
        t *= 2
    return re

def five(k):
    t = 5
    re = 0
    while t<=k:
        re += k//t
        t *= 5
    return re

n,m = map(int,input().split())

print(min(
    two(n)-two(n-m)-two(m),
    five(n)-five(n-m)-five(m)
))