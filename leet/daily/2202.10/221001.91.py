class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*n # i 번째까지 디코딩경우의 수
        dp[0] = 1 if s[0]!='0' else 0
        if n==1:
            return dp[0]
        dp[1] = (1 if 9<int(s[0:2])<27 else 0)+(dp[0] if s[1]!='0' else 0)
        for i in range(2,n):
            dp[i] = (dp[i-1] if s[i]!='0' else 0) + (dp[i-2] if 9<int(s[i-1:i+1])<27 else 0)
        return dp[-1]