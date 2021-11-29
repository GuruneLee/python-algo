case = 0
while True:
    l,p,v = map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    case+=1
    c = v//p
    m = min(l, v%p)
    re = c*l + min(l, v%p)
    ps = f'Case {case}: {re}'
    print(ps)