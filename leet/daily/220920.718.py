# maximum length of repeated subarray
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0]*(m+1), [0]*(m+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                dp[i%2][j]= (dp[(i+1)%2][j-1] + 1) if nums1[i-1]==nums2[j-1] else 0
            ans = max(ans, max(dp[i%2]))
        
        return ans