# 16:49 17:06
for _ in range(int(input())):
    n,m = map(int,input().split())
    l = list(map(int, input().split()))
    dp = [[l[j*m+i] for i in range(m)] for j in range(n)]
    for j in range(n):
        dp[j][0] = l[j*m]
    for i in range(1, m):
        for j in range(n):
            tmp = 0
            if j==0:
                tmp = max(dp[j][i-1], dp[j+1][i-1])
            if j==n-1:
                tmp = max(dp[j-1][i-1], dp[j][i-1])
            if 0<j<n-1:
                tmp = max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1])
            dp[j][i] += tmp
    print(max(list(map(lambda x:x[m-1], dp))))