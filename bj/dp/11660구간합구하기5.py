# 누적합
n, m = list(map(int, input().split()))

l = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    tmpl = list(map(int, input().split()))
    sum = 0
    for j in range(1, n+1):
        sum += tmpl[j-1]
        l[i][j] = sum

for _ in range(m):
    a, b, c, d = list(map(int, input().split()))
    re = 0
    for x in range(a, c+1):
        re += l[x][d] - l[x][b-1]
    print(re)


# 정윤풀이
# 위 옆 누적합
# import sys
# input=sys.stdin.readline
# n, m = map(int,input().split())
# l = [list(map(int, input().split())) for _ in range(n)]

# psum = [[0] * (n+1) for _ in range(n+1)]
# for i in range(n):
#   for j in range(n):
#     psum[i+1][j+1] = psum[i+1][j] + l[i][j]
# for i in range(n):
#   for j in range(n):
#     psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j+1]

# def asum(a, b, c, d):
#   return psum[c][d]-psum[a-1][d]-psum[c][b-1]+psum[a-1][b-1]

# for _ in range(m):
#   x1, y1, x2, y2 = map(int,input().split())
#   print(asum(x1, y1, x2, y2))
