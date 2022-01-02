for _ in range(int(input())):
    n = int(input())
    l = list(input().split())

    s = "" + l[0][0]
    for i in range(1, len(l)):
        if l[i-1][1] == l[i][0]:
            s += l[i][0]
        else:
            s += l[i-1][1]+l[i][0]
    s += l[len(l)-1][1]
    if len(s) < n:
        s += 'a'

    print(s)
