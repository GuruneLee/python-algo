for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int, input().split()))
    l.sort()
    
    i,j = 0,n-1
    diff = int(2e8)
    cnt = 0
    for _ in range(n-1):
        if abs(l[i]+l[j]-k) < diff:
            diff = abs(l[i]+l[j]-k)
            cnt = 1
        elif abs(l[i]+l[j]-k) == diff:
            cnt += 1
        
        if l[i]+l[j] > k:
            j -= 1
        else:
            i += 1
    
    print(cnt)