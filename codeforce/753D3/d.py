for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = input().rstrip()
    B = []
    R = []
    for i in range(n):
        if c[i] == 'B':
            B.append(a[i])
        elif c[i] == 'R':
            R.append(a[i])
    B.sort()
    R.sort(reverse=True)

    flag = True
    for j in range(len(B)):
        if B[j] <= j:
            flag = False

    for j in range(len(R)):
        if R[j] >= n-j+1:
            flag = False

    if flag:
        print("yes")
    else:
        print("no")
