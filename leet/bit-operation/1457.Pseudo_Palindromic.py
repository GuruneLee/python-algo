from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import defaultdict
class Solution:
    def go(self, node, b):
        cnt = 0
        if node.left is None and node.right is None:
            return 1 if b&(b-1)==0 or b==0 else 0
        if node.left:
            cnt += self.go(node.left, b^(2**node.left.val))
        if node.right:
            cnt += self.go(node.right, b^(2**node.right.val))
        return cnt
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.go(root, 2**root.val)
    
## 정수가 2의 거듭제곱인지 판별하기
"""
num&(num-1)==0 이면 num이 2의 거듭제곱이다.

ex. 01100
01100 & 01011 => 01000 != 0
ex. 01000
01000 & 00111 => 00000 == 0
"""