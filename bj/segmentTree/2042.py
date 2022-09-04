import sys
input = lambda: sys.stdin.readline().rstript()

from math import ceil, log2
class segmentTree:
    def __init__(self, origin):
        n = len(origin)
        h = ceil(log2(n))
        t_size = 1 << (h+1)
        self.tree = [0]*t_size  
        self.init(0,n-1,1,origin)
        
    def init(self, start, end, node, origin):
        if (start == end): 
            self.tree[node] = origin[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self.init(start, mid, node*2, l) + self.init(mid+1, end, node*2+1, l)
        return self.tree[node]

    def sum(self, start, end, node, left, right):
        # node 현재 탐색중인 노드 (root 부터 시작)
        # start, end 현재 탐색할 범위 - 현재 node 가 가진 범위 ㅇㅇ
        # left, right 구간합을 구하고싶은 범위
        if end<left or right<start:
            return 0
        if left<=start and end<=right:
            return self.tree[node]
        
        mid = (start + end)//2
        return self.sum(start, mid, node*2, left, right) + self.sum(mid+1, end, node*2+1, left, right)

    def update(self, start, end, node, index, dif):
        # index 바꾸고싶은 값 위치
        # dif 바꿀값-현재값 차이
        if index < start or end < index: return
        self.tree[node] += dif
        if start == end : return
        mid = (start + end)//2
        self.update(start, mid, node*2, index, dif)
        self.update(mid+1, end, node*2+1, index, dif)
        
n,m,k = list(map(int, input().split()))
l = [0]*n
for i in range(n):
    l[i] = int(input())

st = segmentTree(l)
# st.init(0,n-1,1,l)

for _ in range(m+k):
    a,b,c = list(map(int, input().split()))
    if a==1:
        st.update(0,n-1,1,b-1,c-l[b-1])
        l[b-1] = c
    else:
        print(st.sum(0,n-1,1,b-1,c-1))