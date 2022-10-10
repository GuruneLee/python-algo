from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors += ' '
        n = len(colors)
        re = 0
        if n==1:
            return re
        
        i,j = 0,1
        cnt = 1
        while j<n:
            if colors[i]==colors[j]:
                cnt += 1
                j += 1
            else:
                if cnt>1:
                    re += sum(neededTime[i:j])-max(neededTime[i:j])
                i = j
                j += 1
                cnt = 1
        
        return re