n = int(input())

sl = list(input().rstrip() for _ in range(n))
sl.sort(key=lambda x: len(x), reverse=True)
sl = list(map(lambda x: x[::-1], sl))

ml = len(sl[0])
dm = {}
d = 9
sum = 0
for i in range(ml-1, -1, -1):
    tmpS = 0
    for j in range(len(sl)):
        if i < len(sl[j]):
            if sl[j][i] in dm:
                tmpS = tmpS + dm.get(sl[j][i])
            else:
                tmpS += d
                dm.update({sl[j][i]: d})
                d -= 1
    sum += tmpS*pow(10, i)
print(sum)
