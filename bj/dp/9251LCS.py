a = " " + input()
b = " " + input()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(a)-1][len(b)-1])