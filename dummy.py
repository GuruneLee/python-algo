n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = l[0][0]
if n == 1:
    print(l[0][0])
    exit(0)
dp[1][0] = dp[0][0] + l[1][0]
dp[1][1] = dp[0][0] + l[1][1]
for i in range(1, n):
    le = len(l[i])
    for j in range(le):
        if j == 0:
            dp[i][j] = dp[i-1][j] + l[i][j]
            continue
        if j == le-1:
            dp[i][j] = dp[i-1][j-1] + l[i][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + l[i][j]
print(max(dp[n-1][:]))
