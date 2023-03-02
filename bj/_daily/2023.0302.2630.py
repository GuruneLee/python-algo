# 색종이 만들기
## 21:06 ~ 21:26

n = int(input())
ll = [list(map(int,input().split())) for _ in range(n)]
v = {}

def isOneColor(i,j,m,l):
    begin = l[i][j]
    for a in range(i, i+m):
        for b in range(j, j+m):
            if l[a][b] != begin:
                return False
    return True

def go(i,j,m,l):
    if isOneColor(i,j,m,l):
        if l[i][j] == 0:
            return (1,0) # (white, blue)
        else:
            return (0,1)
    
    h = m//2
    r1 = go(i,j,h,l)
    r2 = go(i,j+h,h,l)
    r3 = go(i+h,j,h,l)
    r4 = go(i+h,j+h,h,l)
    
    return (r1[0]+r2[0]+r3[0]+r4[0], r1[1]+r2[1]+r3[1]+r4[1])

r = go(0,0,n,ll)
print(r[0])
print(r[1])