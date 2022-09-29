# Push Dominoes
class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        l = 0
        ans = []
        for r in range(1,n):
            if d[r]=='.':
                continue
            
            between = r-l-1
            # 처음의 경우
            if d[l]=='.' and d[r]=='L':
                ans.extend(['L']*r)
            elif d[l]=='.':
                ans.extend(['.']*r)
            # L...R
            if d[l]=='L' and d[r]=='R':
                ans.append('L')
                ans.extend(['.']*between)
            # R...L
            if d[l]=='R' and d[r]=='L':
                ans.append('R')
                ans.extend(['R']*(between//2))
                if between%2==1: ans.append('.') 
                ans.extend(['L']*(between//2))
            # L...L or R...R
            if d[l]==d[r]:
                ans.extend([d[l]]*(between+1))
            l = r
        
            # print(d[r], ans, l)
        ans.append(d[l])
        num = n-l-1
        if d[l] == 'R':
            ans.extend(['R']*num)
        else:
            ans.extend(['.']*num)
        
        return ''.join(ans)
            
                    
            