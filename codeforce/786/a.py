import math


for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = 0, 0
    flag = False
    if x > y or y % x != 0:
        print(0, 0)
        continue
    else:
        b = y//x
        a = 1
        print(a, b)
