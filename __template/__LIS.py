# Longest Increasing Sequnce
# 최장 증가 수열 찾기

# dp
def lis1(l):
    n = len(l)
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

# seg_tree - 잘 안씀
# dp를 seg_tree로 최적화 하는 방법임 (max_segTree 사용)
## https://m.blog.naver.com/kks227/220791986409 
## - segment tree에 대한 내용 (lis가 포함되어 있음)
## - 문제 추천도 많음
## https://nicotina04.tistory.com/167 - lis에 대한 내용 총망라
from math import log2, ceil
class lisSegmentTree:
    def __init__(self, n):
        self.INF = int(1e9)
        self.tree = [0]*(1<<(1+ceil(log2(n))))
    def findMax(self, s, e, node, l, r):
        if e<l or r<s:
            return -self.INF
        if l<=s and e<=r:
            return self.tree[node]
        m = (s+e)//2
        return max(
            self.findMax(s,m,node*2,l,r),
            self.findMax(m+1,e,node*2+1,l,r)
        )
    def buildTree(self, s, e, node, idx, val):
        if idx<s or e<idx:
            return 0
        if s == e:
            self.tree[node] = max(self.tree[node], val)
            return self.tree[node]
        m = (s+e)//2
        cmp = max(
            self.buildTree(s,m,node*2,idx,val),
            self.buildTree(m+1,e,node*2+1,idx,val)
        )
        self.tree[node] = max(cmp, self.tree[node])
        return self.tree[node]
    
l = [1,2,3,4,5,6,7,8]
idx = [1,2,5,7,6,0,3,4]

n = len(l)
lst = lisSegmentTree(n)
for i in range(n):
    max_ = lst.findMax(0,n-1, 1, 0,idx[i])
    lst.buildTree(0,n-1, 1, idx[i],max_+1)

print(lst.tree[1])