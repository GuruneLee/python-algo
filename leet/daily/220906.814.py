
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root):
        def checkAndRemove(node):
            isRemoved = (node.val == 0)
            leftRemoved = False if node.left else True
            rightRemoved = False if node.right else True
            
            if leftRemoved and rightRemoved:
                return isRemoved
            if not leftRemoved:
                leftRemoved = checkAndRemove(node.left)
                if leftRemoved:
                    node.left = None
            if not rightRemoved:
                rightRemoved = checkAndRemove(node.right)
                if rightRemoved:
                    node.right = None

            return isRemoved and leftRemoved and rightRemoved
        
        if checkAndRemove(root):
            root = None
        
        return root
    
sol = Solution()
ans = sol.pruneTree(
    TreeNode(1,
        None,
        TreeNode(0,
            TreeNode(0),
            TreeNode(1)
        )
    )
) # [1,null,0,0,1] -> [1,null,0,null,1]
def p(root):
    print(root.val, end=", ")
    if root.left: 
        p(root.left)
    else:
        print('null', end=", ")
    if root.right: 
        p(root.right)
    else:
        print('null', end=", ")
p(ans)