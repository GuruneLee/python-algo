# 상자넣기
t = int(input())
nodes = list(map(int, input().split()))

# dp[i] : i번째까지 수열 중 i번째 수를 포함하는 가장 긴 증가하는 부분수열
# dp[i] = MAX(dp[j]+1) s.t. node[j] < node[i], j<i

dp = [0]*t
dp[0] = 1

max = 1
for i in range(1, t):
    tmp = 0
    for j in range(0, i):
        if nodes[i] > nodes[j]:
            tmp = dp[j] if dp[j] > tmp else tmp
    dp[i] = tmp+1
    max = max if dp[i] < max else dp[i]

print(max)
