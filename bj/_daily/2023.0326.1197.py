# 최소 스패닝 트리
from heapq import heappop, heappush
import sys
input=lambda:sys.stdin.readline().rstrip()

class uf:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a] 
    def uinon(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A<B:
            self.parent[A]=B
        else:
            self.parent[B]=A
    def doesMakeCycle(self, a, b):
        return self.find(a)==self.find(b)

v,e = map(int,input().split())
el = []
for _ in range(e):
    a,b,c = map(int,input().split())
    heappush(el, (c,a-1,b-1))

u = uf(v)
w = 0
while el:
    c,a,b = heappop(el)
    if not u.doesMakeCycle(a,b):
        u.uinon(a,b)
        w += c

print(w)