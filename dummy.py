n, m = map(int, input().split())
l = [input() for _ in range(n)]

cn = cm = 0
for i in range(n):
    # print(l[i])
    if 'X' not in l[i]:
        cn += 1

for i in range(m):
    tl = ""
    for j in range(n):
        tl += l[j][i]
    if 'X' not in tl:
        cm += 1
print(max(cn, cm))
