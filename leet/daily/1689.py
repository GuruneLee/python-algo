class Solution:
    def minPartitions(self, n: str) -> int:
        max_ = 0
        for c in str(n):
            max_ = max(max_, int(c))
        return max_
        
s = Solution()
s.minPartitions(82734)