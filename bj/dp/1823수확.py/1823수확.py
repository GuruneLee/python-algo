import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = [-1]
for _ in range(n):
    s.append(int(input()))

dp = [[0]*2001 for _ in range(2001)]

def go(l, r, c):
    if l>r:
        return 0
    if l==r:
        return s[l]*c
    if dp[l][r] == 0:
        dp[l][r] = max(
            go(l+1,r,c+1) + s[l]*c, go(l,r-1,c+1) + s[r]*c
        )
    return dp[l][r]

print(go(1,n,1))