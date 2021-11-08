n = int(input())

dp = [ 0 for _ in range(1001)]

for i in range(1, n+1):
    if i%2 != 0:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + 2
