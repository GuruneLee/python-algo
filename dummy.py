n = int(input())
if n == 1:
    exit(0)


def f(x):
    for i in range(2, n+1, 1):
        if x % i == 0:
            print(i)
            f(x//i)
            break


f(n)
