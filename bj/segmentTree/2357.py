from math import ceil, log2
import sys
input= lambda: sys.stdin.readline().rstrip()
class segmentTree:
    def __init__(self, origin):
        self.INF = 1000000001
        n = len(origin)
        h = ceil(log2(n))
        t_size = 1 << (h+1)
        self.tree = [[self.INF, -self.INF] for _ in range(t_size)]
        self.init(0,n-1,1,origin)
        
    def init(self, start, end, node, origin):
        if (start == end): 
            self.tree[node] = [origin[start],origin[start]]
            return self.tree[node]
        mid = (start + end) // 2
        left, right = self.init(start, mid, node*2, origin), self.init(mid+1, end, node*2+1, origin)
        self.tree[node][0] = max(left[0], right[0])
        self.tree[node][1] = min(left[1], right[1])
        return self.tree[node]

    def min(self, start, end, node, left, right):
        if end<left or right<start:
            return self.INF
        if left<=start and end<=right:
            return self.tree[node][1]
        
        mid = (start + end)//2
        return min(self.min(start, mid, node*2, left, right), self.min(mid+1, end, node*2+1, left, right))
    def max(self, start, end, node, left, right):
        if end<left or right<start:
            return -self.INF
        if left<=start and end<=right:
            return self.tree[node][0]
        
        mid = (start + end)//2
        return max(self.max(start, mid, node*2, left, right), self.max(mid+1, end, node*2+1, left, right))

n,m = map(int,input().split())
l =[0]*n
for i in range(n):
    l[i] = int(input())

st = segmentTree(l)
for _ in range(m):
    a,b = map(int,input().split())
    min_, max_ = st.min(0,n-1,1,a-1,b-1), st.max(0,n-1,1,a-1,b-1)
    print(min_, max_)
        
        

