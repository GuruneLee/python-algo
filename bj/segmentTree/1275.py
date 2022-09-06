from math import ceil, log2
import sys
input= lambda: sys.stdin.readline().rstrip()
# general
class SegTree:
    def __init__(self, n, init_val, fun):
        # init_val 은 fun에 대한 항등원
        t_size = 1 << (1+ceil(log2(n)))
        self.tree = [init_val for _ in range(t_size)]
        self.init_val = init_val
        self.fun = fun
    def update(self, node, start, end, idx, x):
        if idx<start or idx>end:
            return self.init_val
        if start == end:
            self.tree[node] = x
        else:
            mid = (start+end)//2
            l = self.update(node*2, start, mid, idx, x)
            r = self.update(node*2+1, mid+1, end, idx, x)
            self.tree[node] = self.fun(self.tree[node*2], self.tree[node*2+1])
        return self.tree[node]
    def query(self, node, start, end, left, right):
        if right<start or end<left:
            return self.init_val
        if left<=start and end<=right:
            return self.tree[node]
        mid = (start+end)//2
        return self.fun(
            self.query(node*2, start, mid, left, right),
            self.query(node*2+1, mid+1, end, left, right)
        )
        
n,q = map(int,input().split())
l = list(map(int, input().split()))
st = SegTree(n, 0, lambda x,y:x+y)
for i in range(n):
    st.update(1,0,n-1,i,l[i])

for i in range(q):
    x,y,a,b = map(int,input().split())
    if x>y:
        x,y = y,x
    print(st.query(1,0,n-1,x-1,y-1))
    st.update(1,0,n-1,a-1,b)