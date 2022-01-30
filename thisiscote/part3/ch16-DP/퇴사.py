# 13:29 - 13:48
n = int(input())
t, p = [0], [0]
for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

dp = [0]*(n+1)

dp[1] = 0 if t[1]>1 else p[1]

for i in range(1, n+1):
    max_ = 0
    for j in range(i, 0, -1):
        if t[j]<=i-j+1:
            max_ = max(max_, dp[j-1]+p[j])
    dp[i] = max_
print(dp[-1])