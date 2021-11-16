# 이건 많이 나오는거
z = int(input())
i = 1  # group
n = 0  # num of num in group
while True:
    n = (i*(i+1))//2
    if n >= z:
        break
    i += 1
if i % 2 == 0:
    n = z - ((i-1)*i)//2
else:
    n = i-(z - ((i-1)*i)//2)+1
print(str(n)+'/'+str(i-n+1))
