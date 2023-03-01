from types import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current = nums[0]
        ans = nums[0]
        for i in range(1, n):
            current = max(nums[i], current+nums[i])
            ans = max(ans, current)
        return ans
