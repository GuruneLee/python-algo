from tkinter import W


class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        ns = sorted(d.values())
        cnt = 0
        print(ns)
        for i in range(len(ns)-1, 0, -1):
            while ns[i]<=ns[i-1] and ns[i-1]>0:
                ns[i-1] -= 1
                cnt += 1
        print(ns, cnt)
        return cnt
        
            
                

S = Solution()
# S.minDeletions("aab")
# S.minDeletions("aaabbbcc")
# S.minDeletions("ceabaacb")
S.minDeletions("bbcebab")