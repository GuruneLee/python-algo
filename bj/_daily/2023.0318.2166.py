# 다각형의 면적

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
p.append([p[0][0], p[0][1]])

print(p)
x,y = 0,0
for i in range(n):
    x += p[i][0]*p[i+1][1]
    y += p[i][1]*p[i+1][0]
    
t = round(abs((x-y)/2), 1)
print(t)