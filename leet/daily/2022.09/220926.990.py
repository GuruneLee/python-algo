from typing import List

class ufSet:
    def __init__ (self, n):
        self.parent = [i for i in range(n)]
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A<B:
            self.parent[A] = B
        else:
            self.parent[B] = A

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def i(c):
            return ord(c)-ord('a')
        
        equations.sort(key=lambda x: x[1], reverse=True)
        uf = ufSet(26)
        for eq in equations:
            if eq[1]=='=':
                uf.union(i(eq[0]), i(eq[3]))
            else:
                if uf.find(i(eq[0])) == uf.find(i(eq[3])):
                    return False
        return True