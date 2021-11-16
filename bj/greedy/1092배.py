cn = int(input())  # 크레인 수
wl = list(map(int, input().split()))
bm = int(input())  # 박스 수
w = list(map(int, input().split()))

wl.sort(reverse=True)
w.sort(reverse=True)

if wl[0] < w[0]:
    print(-1)
    exit(0)

v = [0]*cn
i, j = 0, 0
for i in range(bm):
    mj = -1
    for j in range(cn):
        if wl[j] >= w[i]:
            if mj == -1:
                mj = j
            if v[mj] > v[j]:
                mj = j
    v[mj] += 1


print(max(v))
