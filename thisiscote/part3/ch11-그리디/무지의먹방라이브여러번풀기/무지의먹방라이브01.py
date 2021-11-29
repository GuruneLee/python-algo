def solution(l, k):
    n = len(l) #전체음식개수
    f = [] #음식개수 / 음식번호
    for i in range(len(l)):
        f.append((l[i], i+1))
    f.sort(key=lambda x: x[0])
    
    pre = 0
    for i in range(len(f)):
        amount, number = f[i]
        dif = amount-pre
        tmp = dif*n
        if tmp<=k:
            pre = amount
            k -= tmp
        else:
            k = k%n
            sub = sorted(f[i:], key=lambda x:x[1])
            return sub[k][1]
        n -= 1
    
    return -1

LIST = [3,1,2]
K = 5
print(solution(LIST,K))
        