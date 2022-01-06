m = int(input())
n = int(input())


def prime_list(s, x):
    sieve = [True]*x
    tmp = int(x**0.5)
    for i in range(2, tmp+1):
        if sieve[i]:
            for j in range(i+i, x, i):
                sieve[j] = False
    return [i for i in range(2, x) if sieve[i] and i >= s]


p = prime_list(m, n+1)
if len(p) != 0:
    print(sum(p))
    print(min(p))
else:
    print(-1)
