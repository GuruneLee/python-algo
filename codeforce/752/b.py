t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) % 2 == 0:
        print("YES")
    else:
        flag = False
        for i in range(1, len(a)):
            if a[i-1] >= a[i]:
                print("YES")
                flag = True
                break
        if not flag:
            print("NO")
