from math import ceil, log2
import sys
input= lambda: sys.stdin.readline().rstrip()
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
        self.tree[node] = self.init(start, mid, node*2, origin) + self.init(mid+1, end, node*2+1, origin)
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
        
        
        
l = [1,9,3,8,4,5,5,9,10,3,4,5]
st = segmentTree(len(l))
st.init(0,11,1,l)

print(st.sum(0,11,1,0,2))
st.update(0,11,1,0,10)
print(st.sum(0,11,1,0,2))

