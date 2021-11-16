# dp[i][0] : i 번째 계단을 밟았을 때, 점수의 최댓값 (i-1 을 밟지 않음)
# dp[i][1] : i 번째 계단을 밟았을 때, 점수의 최댓값 (i-1 을 밟음)
# dp[i][0]
#   = m[i] + MAX(dp[i-2][0], dp[i-2][1])
# dp[i][1]
#   = m[i] + dp[i-1][0]


n = int(input())
m = [0, ]
for _ in range(n):
    m.append(int(input()))

dp = [
    [0, 0],
    [m[0], m[0]],
    [m[1], m[0]+m[1]]
]

for i in range(3, n+1):
    tmp1 = m[i] + max(dp[i-2][0], dp[i-2][1])
    tmp2 = m[i] + dp[i-1][0]
    dp.append([tmp1, tmp2])

print(max(dp[n][0], dp[n][1]))
