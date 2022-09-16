class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& mul) {
        int n = nums.size();
        int m = mul.size();

        vector<vector<int>> dp(m+1, vector<int>(m+1, 0));
        for (int i=1;i<m+1; i++) {
            dp[i][0] = dp[i-1][0] + mul[i-1]*nums[i-1];
            dp[0][i] = dp[0][i-1] + mul[i-1]*nums[n-i];
        }
        int ans = max(dp[m][0], dp[0][m]);
        for (int i=1; i<m+1; i++) {
            for (int j=1; j<m-i+1; j++) {
                int left = dp[i-1][j]+mul[i+j-1]*nums[i-1];
                int right = dp[i][j-1]+mul[i+j-1]*nums[n-j];
                dp[i][j] = max(left, right);
                if (i+j==m)
                    ans = max(ans, dp[i][j]);
            }
        }
        
        return ans;
    }
};