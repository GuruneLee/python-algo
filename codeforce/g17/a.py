for _ in range(int(input())):
    n, m = map(int,input().split())
    tmp = min(n,m)
    if n==1 and m==1:
        print(0)
    elif tmp == 1:
        print(1)
    else:
        print(2)