from math import ceil, log2
class segmentTree:
    def __init__(self, origin):
        n = len(origin)
        h = ceil(log2(n))
        t_size = 1 << (h+1)
        self.tree = [1000000001]*t_size  
        self.init(0,n-1,1,origin)
        
    def init(self, start, end, node, origin):
        if (start == end): 
            self.tree[node] = origin[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = min(self.init(start, mid, node*2, l), self.init(mid+1, end, node*2+1, l))
        return self.tree[node]

    def min(self, start, end, node, left, right):
        # node 현재 탐색중인 노드 (root 부터 시작)
        # start, end 현재 탐색할 범위 - 현재 node 가 가진 범위 ㅇㅇ
        # left, right 구간합을 구하고싶은 범위
        if end<left or right<start:
            return 1000000001
        if left<=start and end<=right:
            return self.tree[node]
        
        mid = (start + end)//2
        return min(self.min(start, mid, node*2, left, right), self.min(mid+1, end, node*2+1, left, right))
        
n,m = map(int,input().split())
l =[0]*n
for i in range(n):
    l[i] = int(input())

st = segmentTree(l)
for _ in range(m):
    a,b = map(int,input().split())
    print(st.min(0,n-1,1,a-1,b-1))
    