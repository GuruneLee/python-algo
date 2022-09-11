# maximum peformance of a team
from heapq import heappush, heappop
from types import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = int(1e9)+7
        l = [[speed[i],efficiency[i]] for i in range(n)]
        l.sort(key=lambda x: (-x[1], x[0]))
        
        hq = []
        sum_ = 0
        ans = 0
        
        for i in range(0, n):
            if len(hq)==k:
                sum_ -= heappop(hq)
            sum_ += l[i][0]
            heappush(hq, l[i][0])
            ans = max(ans, sum_*l[i][1])
        
        return ans%mod