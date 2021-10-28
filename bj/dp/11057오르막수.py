# dp[i][j] : i자리에 j로 끝나는 오르막 수의 개수
# dp[i][j] = dp[i-1][j] + ... + dp[i-1][9]
N = int(input())
dp = [[0]*10  for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1


for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])

print(sum(dp[N][0:10])%10007)
