for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    if l[0]+l[1]+l[2] == l[6]:
        print(l[0], l[1], l[2])
    else:
        print(l[0], l[1], l[3])
