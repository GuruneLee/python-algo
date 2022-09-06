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
        
l = [1,9,3,8,4,5,5,9,10,3,4,5]
length = len(l)
# 합 seg tree
init_val = 0
sum_fun = lambda x,y: x+y
st = SegTree(length, init_val, sum_fun)
for i in range(length):
    st.update(1, 0, length-1, i, l[i])
print(st.query(1, 0, length-1, 0,2)) 

# 곱 seg tree
init_val = 1
mul_fun = lambda x,y: x*y
st = SegTree(length, init_val, mul_fun)
for i in range(length):
    st.update(1,0,length-1,i,l[i])
print(st.query(1,0,length-1,1,3))

# max seg tree
init_val = -int(1e9)
max_fun = max
st = SegTree(length, init_val, max_fun)
for i in range(length):
    st.update(1,0,length-1,i,l[i])
print(st.query(1,0,length-1,1,3))


# class segmentTree:
#     def __init__(self, origin):
#         n = len(origin)
#         h = ceil(log2(n))
#         t_size = 1 << (h+1)
#         self.tree = [0]*t_size  
#         self.init(0,n-1,1,origin)
        
#     def init(self, start, end, node, origin):
#         if (start == end): 
#             self.tree[node] = origin[start]
#             return self.tree[node]
#         mid = (start + end) // 2
#         self.tree[node] = self.init(start, mid, node*2, origin) + self.init(mid+1, end, node*2+1, origin)
#         return self.tree[node]

#     def sum(self, start, end, node, left, right):
#         # node 현재 탐색중인 노드 (root 부터 시작)
#         # start, end 현재 탐색할 범위 - 현재 node 가 가진 범위 ㅇㅇ
#         # left, right 구간합을 구하고싶은 범위
#         if end<left or right<start:
#             return 0
#         if left<=start and end<=right:
#             return self.tree[node]
        
#         mid = (start + end)//2
#         return self.sum(start, mid, node*2, left, right) + self.sum(mid+1, end, node*2+1, left, right)

#     def update(self, start, end, node, index, dif):
#         # index 바꾸고싶은 값 위치
#         # dif 바꿀값-현재값 차이
#         if index < start or end < index: return
#         self.tree[node] += dif
#         if start == end : return
#         mid = (start + end)//2
#         self.update(start, mid, node*2, index, dif)
#         self.update(mid+1, end, node*2+1, index, dif)
        
        
        
# l = [1,9,3,8,4,5,5,9,10,3,4,5]
# st = segmentTree(l)
# st.init(0,11,1,l)

# print(st.sum(0,11,1,0,2))
# st.update(0,11,1,0,10)
# print(st.sum(0,11,1,0,2))
