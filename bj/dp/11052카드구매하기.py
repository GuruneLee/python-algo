n = int(input())
p = list(map(int, input().split()))

# dp[a] : a개를 구매한 최대 가격
# dp[a] = max(dp[a-c] + c카드팩가격), 1<=c<=a
dp = [0 for _ in range(n+1)]
dp[1] = p[0]

for i in range(2,n+1):
    MAX = 0
    for c in range(1,i+1):
        MAX = max(MAX, dp[i-c]+p[c-1])
    dp[i] = MAX
print(dp[n])