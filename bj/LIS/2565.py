# seg_tree
# dp를 seg_tree로 최적화 하는 방법임 (max_segTree 사용)
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
    
n = int(input())
l = []
for i in range(n):
    a, b = map(int,input().split())
    l.append([b,a])
l.sort(key=lambda x: x[1])
for i in range(n):
    l[i][1] = i
l.sort(key=lambda x: (x[0], -x[1]))

lst = lisSegmentTree(n)
for i in range(n):
    idx = l[i][1]
    max_ = lst.findMax(0,n-1,1,0,idx)
    lst.buildTree(0,n-1,1,idx,max_+1)

print(n-lst.tree[1])