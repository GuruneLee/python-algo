from types import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def go(val):
            ans = -1
            if val>>7==0:
                ans = 0
            if val>>5==6:
                ans = 1
            if val>>4==14:
                ans = 2
            if val>>3==30:
                ans = 3
            if val>>6==2:
                ans = 5
            return ans
        n = len(data)
        
        cnt = 0
        i = 0
        while i<n:
            if cnt==0:
                cnt = go(data[i])
                if cnt==-1 or cnt==5: return False
                i += 1
            if i>=n:
                break
            while cnt>0:
                if go(data[i])!=5: return False
                cnt -= 1
                i += 1

        return True if cnt==0 and i==n else False