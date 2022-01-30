# 17:30 x(혼자힘으로 못품)

sa = input()
sb = input()

dp = [[0]*(len(sb)+1) for _ in range(len(sa)+1)]
for i in range(len(sb)+1):
    dp[0][i] = i
for i in range(len(sa)+1):
    dp[i][0] = i

# dp[i][j] = sa[:i+1]에서 sb[:j+1]로의 편집거리
for i in range(1, len(sa)+1):
    for j in range(1, len(sb)+1):
        if sa[i-1] == sb[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],
                           dp[i-1][j],
                           dp[i][j-1]) + 1

print(dp[len(sa)][len(sb)])
