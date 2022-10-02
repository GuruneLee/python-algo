# Trapping Rain Water
from typing import List

class Solution:
    def getSum(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        s = []
        sum_ = 0
        for i in range(1,n):
            if height[i]<height[l]:
                s.append(height[i])
            else:
                while s:
                    sum_ += height[l]-s.pop()
                l = i
        return sum_
    
    def trap(self, height):
        max_ = max(height)
        l_max = height.index(max_)
        r_max = len(height) - height[-1::-1].index(max_) - 1
        
        total_sum = max_*(r_max-l_max-1)-sum(height[l_max+1:r_max])
        if total_sum<0: total_sum = 0
        # print(total_sum)
        total_sum += self.getSum(height[:l_max+1])
        total_sum += self.getSum(height[r_max:][::-1])
        
        return total_sum