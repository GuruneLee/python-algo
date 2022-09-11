n,m = map(int,input().split())
l = [int(input()) for _ in range(n)]
l.sort()

# iterator
l_iter = iter(l)
r_iter = iter(l)
left, right = next(l_iter), next(r_iter)
min_dif = 1000000001
ans = 0
while right is not None:
    diff = right-left
    if m <= diff < min_dif:
        min_dif = diff
        ans += 1
    if diff > m:
        # diff==m 일땐, right를 늘려서 더 큰 차를 찾아야함
        left = next(l_iter)
    else:
        # 다음 right가 없다면, diff는 커질 수 없음
        right = next(r_iter, None)
print(min_dif)

# indexing
i,j = 0,0
min_ = int(2e9)
while j<n:
    dif = l[j]-l[i]
    if min_>dif>=m:
        min_ = dif
    if dif>m:
        i+=1
    else:
        j+=1
print(min_)