def f(x): # x짜리 별찍기
    m = [[0]*x for _ in range(x)]
    p = [(0,0),       (0,x//3),       (0,(x//3)*2),
         (x//3,0),                    (x//3,(x//3)*2),
         ((x//3)*2,0),((x//3)*2,x//3),((x//3)*2,(x//3)*2)]
    
    frag = []
    if x==9:
        frag = [['*','*','*'],['*',' ','*'],['*','*','*']]
    else:
        frag = f(x//3)
    
    for i in range(len(p)):
        sx, sy = p[i]
        for dx in range(x//3):
            for dy in range(x//3):
                cx = sx+dx
                cy = sy+dy
                m[cx][cy] = frag[dx][dy]
    
    return m


def print_(l, n):
    for i in range(n):
        for j in range(n):
            print(l[i][j] if l[i][j]!=0 else ' ', end=" ")
        print()

n = int(input())

if n==3:
    print_([['*','*','*'],['*',' ','*'],['*','*','*']], n)
else:
    print_(f(n), n)