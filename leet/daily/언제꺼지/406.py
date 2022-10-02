
class Solution:
    def reconstructQueue(self, p):
        p = sorted(p, key=lambda x : (-x[0], x[1]))
        ans = []
        for i in range(0, len(p)):
            ans.insert(p[i][1], p[i])
            print(ans)
        return
        
p = [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
s = Solution()
s.reconstructQueue(p)
