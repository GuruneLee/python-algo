# 별찍기 - 11
## 22:58 ~ 
import math

N = int(input()) # 3*(2**k)
K = int(math.log(n//3,2))

def p(str):
    print(str, end='')

def one(n, space):
    one(n//2, space+n//2)
    two(n//2, space)
    return
def two(n, space):
    return