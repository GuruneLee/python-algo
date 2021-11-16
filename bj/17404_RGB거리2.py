n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

dp = [list([0, 0, 0]) for i in range(n)]

# 처음 시작이 0 일 때
MAX = 1000005
re = 1000005

# 첫집에 k색 칠했을 때
for k in range(3):
    dp[0][0] = MAX
    dp[0][1] = MAX
    dp[0][2] = MAX
    dp[0][k] = m[0][k]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + m[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + m[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + m[i][2]
    for i in range(3):
        if (i == k):
            continue
        re = min(re, dp[n-1][i])

print(re)
