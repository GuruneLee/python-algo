for _ in range(int(input())):
    x, n = list(map(int, input().split()))
    re = 0
    if n % 4 == 1:
        re = (-1)*n
    elif n % 4 == 2:
        re = 1
    elif n % 4 == 3:
        re = 1+n
    elif n % 4 == 0:
        re = 0

    if x % 2 != 0:
        re = (-1)*re
    print(x+re)
