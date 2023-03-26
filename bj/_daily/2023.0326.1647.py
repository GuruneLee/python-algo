# 도시 분할 계획
import sys
from heapq import heappop, heapify
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
    
n,m = map(int,input().split())

el = []
for _ in range(m):
    a,b,c = map(int,input().split())
    el.append((c,a-1,b-1))
heapify(el)

u = uf(n)
w = 0
m = 0
while el:
    c,a,b = heappop(el)
    if not u.doesMakeCycle(a,b):
        u.uinon(a,b)
        w += c
        m = c
    
print(w-m)