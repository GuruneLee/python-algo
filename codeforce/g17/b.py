for _ in range(int(input())):
    n = int(input())
    if n==0 or n==1 or n==2:
        print("YES")
        continue
    l = list(map(int, input().split()))