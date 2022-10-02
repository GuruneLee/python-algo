# find duplicate file in system
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, p: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        n = len(p)
        for i in range(n):
            l = p[i].split(' ')
            it = iter(l[1:])
            current = next(it, None)
            print(l[0])
            while current:
                content = current.split('(')[1][:-1]
                print(content)
                d[content].append(l[0]+"/"+current.split('(')[0])
                current = next(it, None)
        return list(filter(lambda x: len(x)>1, d.values()))