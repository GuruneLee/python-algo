a, b, c = map(int, input().split())

# 정수론에 가까운 무언가?
d = {}
d[0] = 1
d[1] = a % c
d[2] = (a**2) % c


def cal(x):
    if x == 0:
        return d[0]
    if x == 1:
        return d[1]
    elif x == 2:
        return d[2]

    if x//2 not in d:
        d[x//2] = cal(x//2) % c
    if x % 2 == 0:
        d[x] = d[x//2] * d[x//2]
    else:
        d[x] = d[x//2] * d[x//2] * a % c
    d[x] = d[x] % c
    return d[x]


print(cal(b))
