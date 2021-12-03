n = int(input())
l = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    l.append((x, y))
l.sort()

# 메모리 덜쓰는 버젼
ans = 0
re = (0, 0)
for i in range(len(l)):
    lx, ly = re
    cx, cy = l[i]
    if ly <= cx:
        ans += 1
        re = l[i]
    elif cy <= ly:
        re = l[i]
print(ans)
# 날림 버젼
# re = [(0, 0)]
# for i in range(len(l)):
#     lx, ly = re[len(re)-1]
#     cx, cy = l[i]
#     if ly <= cx:
#         re.append((cx, cy))
#     elif cy <= ly:
#         re.pop()
#         re.append((cx, cy))
# print(len(re)-1)
