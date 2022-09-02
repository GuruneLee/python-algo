from math import floor


class Solution:
    def minMoves2(self, nums) -> int:
        nums = sorted(nums)
        n = len(nums)
        b = nums[0]
        if n%2==0:
            b = nums[n//2]
        else:
            b = nums[(n-1)//2]
        return sum(map(lambda x: abs(x-b), nums))
    
s=Solution()
print(s.minMoves2([1,2,3]))
print(s.minMoves2([1,10,2,9]))