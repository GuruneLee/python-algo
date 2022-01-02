for _ in range(int(input())):
    end = False
    n = int(input())
    l = list(map(int, input().split()))
    d0 = {1}  # 1,3,5,
    d1 = {1}  # 0,2,4,

    for i in range(1, l[0]+1):
        if l[0] % i == 0:
            d0.add(i)
            d0.add(l[0]//i)
    for i in range(1, l[1]+1):
        if l[1] % i == 0:
            d1.add(i)
            d1.add(l[1]//i)

    d0 = list(d0)
    d1 = list(d1)
    # print(d0, d1)

    f1 = False
    f2 = False

    dd0 = []
    for d in d0:
        f = True
        for i in range(2, len(l), 2):
            if l[i] % d != 0:
                f = False
                break
        if f:
            dd0.append(d)
    dd1 = []
    for d in d1:
        f = True
        for i in range(3, len(l), 2):
            if l[i] % d != 0:
                f = False
                break
        if f:
            dd1.append(d)

    # print(dd0, dd1)

    ld = list(set(dd0).difference(dd1))
    rd = list(set(dd1).difference(dd0))
    for d in ld:
        f = True
        for i in range(1, len(l), 2):
            if l[i] % d == 0:
                f = False
                break
        if not f:
            continue
        else:
            print(d)
            end = True
            break
    if end:
        continue
    for d in rd:
        f = True
        for i in range(2, len(l), 2):
            if l[i] % d == 0:
                f = False
                break
        if not f:
            continue
        else:
            print(d)
            end = True
    if end:
        continue

    print(0)
