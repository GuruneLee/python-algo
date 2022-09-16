class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        n = len(nums)
        m = len(mul)
        print(n,m)

        dp = [[0]*(m+2) for _ in range(m+2)]
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] + mul[i-1]*nums[i-1]
            dp[0][i] = dp[0][i-1] + mul[i-1]*nums[n-i]
        ans = max(dp[m][0], dp[0][m])
        for i in range(1,m+1):
            for j in range(1,m-i+1):
                left = dp[i-1][j]+mul[i+j-1]*nums[i-1]
                right = dp[i][j-1]+mul[i+j-1]*nums[n-j]
                dp[i][j] = max(left, right)
                if i+j==m:
                    ans = max(ans, dp[i][j])
        return ans