
from collections import defaultdict
from math import ceil, log2
import sys
input= lambda: sys.stdin.readline().rstrip()
class segmentTree:
    def __init__(self, origin):
        n = len(origin)
        h = ceil(log2(n))
        t_size = 1 << (h+1)
        self.idxOfMin = {}
        self.tree = [0]*t_size  # [0]-sum, [1]-min
        self.init(0,n-1,1,origin)
        
    def init(self, start, end, node, origin):
        if (start == end): 
            self.tree[node] = origin[start]
            self.idxOfMin[self.tree[node]] = (start, end)
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = min(self.init(start, mid, node*2, origin),self.init(mid+1, end, node*2+1, origin))
        self.idxOfMin[self.tree[node]] = (start, end)
        return self.tree[node]
    def min(self, start, end, node, left, right):
        if end<left or right<start:
            return 1000001
        if left<=start and end<=right:
            return self.tree[node]
        mid = (start + end)//2
        return min(self.min(start, mid, node*2, left, right), self.min(mid+1, end, node*2+1, left, right))
    def rerange(self, l):
        ms = []
        for k in range(len(l)):
            while ms and ms[-1]>=l[k]:
                num = ms.pop()
                r2 = self.idxOfMin[num]
                r1 = self.idxOfMin[l[k]]
                # if r1 이 r2 를 포함하지 않으면:
                #     r1의 범위가 r2를 포함하도록 수정
                if not (r1[0]<=r2[0] and r2[1]<=r1[1]):
                    self.idxOfMin[l[k]] = (min(r2[0], r1[0]), max(r2[1], r1[1]))
                    
            ms.append(l[k])
        
n = int(input())
l = list(map(int, input().split()))
st = segmentTree(l)
st.rerange(l)
st.rerange(list(reversed(l)))
preSum = [l[i] for i in range(n)]
for i in range(1,n):
    preSum[i] = preSum[i-1] + l[i]
print(preSum)
re = 0
for k in range(n):
    i, j = st.idxOfMin[l[k]]
    sum_ = preSum[j] - preSum[i-1] if i!=0 else 0
    print(l[k], i, j, l[k]*sum_)
        