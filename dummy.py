n, k = map(int, input().split())

w = []
for _ in range(n):
    w.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    for j in range(1, k+1):
        if j >= w[i]:
            dp[j] += dp[j-w[i]]

print(dp[k])
