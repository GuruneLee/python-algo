## [Largest_Palindromic_Number](https://leetcode.com/submissions/detail/787202932/)

class Solution:
    def largestPalindromic(self, num: str) -> str:
        d = [0]*10
        for i in list(num):
            d[int(i)] += 1
        
        p = list(map(lambda x:x//2, d))
        m = list(map(lambda x:x%2, d))
        
        r = ""
        mid = -1
        for i in range(9,-1,-1):
            if not r and i>0:
                while(p[i]>0):
                    r += str(i)
                    p[i]-=1
            if r:
                while(p[i]>0):
                    r += str(i)
                    p[i]-=1
            if mid==-1 and m[i]==1:
                mid = i
        t = r[::-1]
        r += str(mid) if mid!=-1 else ""
        r += t
        
        return r if r else "0"
