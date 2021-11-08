# n, list
n = int(input())
l = list(map(int, input().split()))

# t, n, list
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

# n, n 개의 list
n = int(input())
ll = [map(int, input().split()) for _ in range(n)]

# 두 수의 최대공약수


def gcd(a, b):
    while b > 0:
        r = n % a
        a = b
        b = r
    return a


def lcm(a, b):
    g = gcd(a, b)
    return (a*b)//g
