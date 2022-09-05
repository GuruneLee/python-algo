class ufSet:
    def __init__ (self, n):
        self.parent = [0]*n
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

        