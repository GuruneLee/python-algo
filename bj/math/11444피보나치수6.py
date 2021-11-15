# 피보나치수6
# 수학 - 행렬
# 1 1 x f(n-1) = f(n-1) + f(n-2) = f(n)
# 1 0   f(n-2)   f(n-1)            f(n-1)

import sys
sys.setrecursionlimit(10000)

mod = 1000000007
n = int(input())


def calM(a, b):
    return [
        (a[0]*b[0] + a[1]*b[2]) % mod,
        (a[0]*b[1] + a[1]*b[3]) % mod,
        (a[2]*b[0] + a[3]*b[2]) % mod,
        (a[2]*b[1] + a[3]*b[3]) % mod
    ]


def Mat(k):
    if k == 0:
        return [1, 1, 1, 1]
    if k == 1:
        return [1, 1, 1, 0]
    if k % 2 == 0:
        tmp = Mat(k//2)
        return calM(tmp, tmp)
    else:
        tmp = Mat(k-1)
        return calM(tmp, [1, 1, 1, 0])


m = Mat(n-1)
print(m[0] % mod)
