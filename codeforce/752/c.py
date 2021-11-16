t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    y = True
    for i in range(n):
        if a[i] % 2 != 0:
            continue
        y = False
        for x in range(2, i+3):
            if a[i] % x == 0:
                continue
            else:
                y = True
                break
        if not y:
            break
    if y:
        print("YES")
    else:
        print("NO")
