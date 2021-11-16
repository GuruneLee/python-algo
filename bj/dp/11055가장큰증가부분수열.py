n = int(input())
arr = list(map(int, input().split()))

dp = list(arr)

if (n == 1):
    print(arr[0])
    exit(0)

for i in range(1,n):
    for j in range(0,i):
        if (arr[i] > arr[j]):
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp[:n]))