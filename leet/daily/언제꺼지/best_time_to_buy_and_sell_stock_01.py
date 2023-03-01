# 분류가 dp인데
# dp 문제가 아니라 two pointer 같은디
from types import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        
        i,j = 0,1
        max_diff = 0
        while j<n:
            diff = prices[j] - prices[i]
            if diff>0:
                max_diff = max(diff, max_diff)
                j += 1
            else:
                i = j
                j += 1
        return max_diff

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))