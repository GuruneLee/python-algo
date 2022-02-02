# 일차원 배열 (답)
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

# 이차원 배열 (메모리초과)
# # n, k = map(int, input().split())
# # w = [-1]
# # for _ in range(n):
# #     w.append(int(input()))

# # dp = [[0]*(k+1) for _ in range(n+1)]
# # for i in range(n+1):
# #     dp[i][0] = 1

# # for i in range(1, n+1):
# #     for j in range(1, k+1):
# #         dp[i][j] += dp[i-1][j]
# #         if j >= w[i]:
# #             dp[i][j] += dp[i][j-w[i]]

# # print(dp)
