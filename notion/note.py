# 문자열 사전 순
# BA > BB - 문자가 큰게 더 큼
# AA > A - 크기가 다르고 비교가 불가능 하면 긴게 더 큼
# Aa > AAa - 크기가 다르면 앞에서부터 문자가 큰게 더 큼
# 관련 문제 - 백준 1294 문자열장식

# 누적합 문제 - 이중 누적합
# 백준 11660
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

psum = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = psum[i+1][j] + l[i][j]
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j+1]


def asum(a, b, c, d):
    return psum[c][d]-psum[a-1][d]-psum[c][b-1]+psum[a-1][b-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(asum(x1, y1, x2, y2))
