class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = int(1e9)+7
        dp = [[0]*(target+1) for _ in range(n+1)]
        for i in range(1, min(k,target)+1):
            dp[1][i] = 1
        
        for i in range(2,n+1):
            for j in range(1,target+1):
                for x in range(1,k+1):
                    if j-x<=0: break
                    dp[i][j] = (dp[i][j] + dp[i-1][j-x])%mod
        
        return dp[n][target]