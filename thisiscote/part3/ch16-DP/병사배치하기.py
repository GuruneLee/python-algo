# 14:28 - 14:42
n = int(input())
l = list(map(int, input().split()))

## n**2 방법
## dp[i] : l[i] 가 마지막 원소인 가장 긴 감소하는 수열의 길이
dp = [1]*n
for i in range(1, n):
    max_ = 0
    for j in range(i):
        if l[j]>l[i]:
            max_ = max(max_, dp[j])
    dp[i] = max_ + 1

print(n-max(dp))