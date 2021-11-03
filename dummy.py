n = 5
l = list(map(int, input().split()))


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return (a*b)//gcd(a, b)


m = 987654321
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            l1 = l[i]
            l2 = l[j]
            l3 = l[k]
            ll = lcm(l1, lcm(l2, l3))
            m = min(m, ll)
print(m)
