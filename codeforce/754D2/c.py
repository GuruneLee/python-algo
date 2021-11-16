for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        if s[i] == 'a':
            a.append(i)
    if len(a) == 1 or len(a)==0:
        print(-1)
        continue
    m = len(s)
    for i in range(1, len(a)):
        if a[i] - a[i-1] + 1 == 2:
            m = min(m,2)
            break
        elif a[i] - a[i-1] + 1 == 3:
            m = min(m,3)
        elif a[i] - a[i-1] + 1 == 4:
            b=c=0
            for k in range(a[i-1]+1, a[i]):
                if s[k] == 'b': b+=1
                if s[k] == 'c': c+=1
            if b==1:
                m = min(m,4)
    if len(a)>2:
        for i in range(2, len(a)):
            if a[i]-a[i-1]==3 and a[i-1]-a[i-2]==3:
                b=c=0
                for k in range(a[i-1]+1, a[i]):
                    if s[k] == 'b': b+=1
                    if s[k] == 'c': c+=1
                if b==1:
                    continue
                for k in range(a[i-2]+1, a[i-1]):
                    if s[k] == 'b': b+=1
                    if s[k] == 'c': c+=1
                if b==2:
                    m = min(m,7 )
    print(m)