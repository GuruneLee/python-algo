# 이분탐색 어려워
N = int(input())
k = int(input())

s = 1
e = k


def O(m):
    cnt = 0
    for mod in range(1, N+1):
        cnt += min(N, m//mod)
    return cnt


re = 0
while s <= e:
    mid = (s+e)//2
    cnt = O(mid)

    if cnt >= k:
        re = mid
        e = mid-1
    else:
        s = mid+1

print(re)
