from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def save(root, d, k):
            if root is None:
                return False
            if k-root.val in d:
                return True
            d.add(root.val)
            return save(root.left, d, k) or save(root.right, d, k)
        
        d = set()
        ans = save(root, d, k)

        return ans