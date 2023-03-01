class ufSet:
    def __init__ (self, n):
        self.parent = [i for i in range(n)]
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        # return self.find(self.parent[a])
        
    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A<B:
            self.parent[A] = B
        else:
            self.parent[B] = A

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # 각 nums 를 index로 바꿔서 저장
        d = defaultdict(int)
        idx = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = idx
                idx += 1

        # nums 원소 -1/+1 숫자(연속된 숫자)의 index를 union
        # 같은 부모를 가진 그룹 => consecutive sequence
        uf = ufSet(idx)
        for i in range(len(nums)):
            if nums[i]+1 in d:
                uf.union(d[nums[i]+1], d[nums[i]])
            if nums[i]-1 in d:
                uf.union(d[nums[i]-1], d[nums[i]])

        # 같은 그룹 중 가장 큰 그룹의 길이 찾기
        c = defaultdict(int)
        for i in range(idx):
            c[uf.find(i)] += 1
        
        return max(c.values())
