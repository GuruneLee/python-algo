# 파이프 옮기기
import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
ll = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*n for _ in range(n)] for _ in range(3)] 
# dp[a][b][c] (0<=a<3 0<=b,c<n): 상태가 a이고 끝이 (b,c) 인 상태까지 도달하는데까지 경우의 수
# 0: 가로, 1: 세로, 2: 대각선

dp[0][0][1] = 1
for i in range(2,n):
    if ll[0][i] == 1:
        continue
    dp[0][0][i] = dp[0][0][i-1]
    
for i in range(1,n):
    for j in range(1,n):
        if ll[i][j]==0 and ll[i][j-1]==0 and ll[i-1][j]==0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if ll[i][j]==0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
            
print(sum([dp[k][n-1][n-1] for k in range(3)]))