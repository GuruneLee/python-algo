from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    ## dictionary 풀이
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        cnt = 0
        def go(node):
            cnt = 0
            if node.left is None and node.right is None:
                odd = 0
                for v in d.values():
                    odd += 1 if v%2==1 else 0
                if odd==0 or odd==1:
                    return 1
                else: 
                    return 0
            if node.left:
                d[node.left.val] += 1
                cnt += go(node.left)
                d[node.left.val] -= 1
            if node.right:
                d[node.right.val] += 1
                cnt += go(node.right)
                d[node.right.val] -= 1
            return cnt
        d[root.val] += 1
        return go(root)
    
    ## bit 연산 풀이
    def go(self, node, b):
        cnt = 0
        if node.left is None and node.right is None:
            return 1 if b&(b-1)==0 or b==0 else 0
        if node.left:
            cnt += self.go(node.left, b^(2**node.left.val))
        if node.right:
            cnt += self.go(node.right, b^(2**node.right.val))
        return cnt
    def pseudoPalindromicPaths_bit (self, root: Optional[TreeNode]) -> int:
        return self.go(root, 2**root.val)
