n = int(input())
dw = [list(map(int, input().split())) for _ in range(n)]

dw.sort(key=lambda x: x[0])
print(dw)

maxDay = dw[0][0]
for i in range(1,n):
    maxDay = max(maxDay, dw[i][0])

sum = 0
for day in range(1,maxDay):
    MAX = 0
    for i in range(n):
        if dw[i][1]==0 or dw[i][0]-day < 0: 
            continue
        if MAX < dw[i][1]:
            MAX = dw[i][1]
            MAXI = i
    dw[MAXI][1] = 0
    print(dw[MAXI][0], MAX)
    sum += MAX

print(sum)


# 1 20
# 2 50
# 3 30
# 4 10
# 4 40
# 4 60
# 6 5

# 4 60
# 2 50
# 4 40
# 3 30
# 1 20
# 4 10
# 6 5