# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def append(self, dic, tup):
        if tup[0] not in dic:
            dic[tup[0]] = [tup[1]]
        else:
            dic[tup[0]].append(tup[1])

    def levelOrder(self, root):
        ans = []
        if root == None:
            return ans
        d = {}
        q = Queue()
        q.put((0, root))
        d[0] = [root.val]
        while not q.empty():
            c = q.get()
            cs = c[0]
            cn = c[1]
            cl = cn.left
            cr = cn.right
            if cl != None:
                q.put((cs+1, cl))
                self.append(d, (cs+1, cl.val))
            if cr != None:
                q.put((cs+1, cr))
                self.append(d, (cs+1, cr.val))

        return ans


node = TreeNode(3, TreeNode(9, None, None), TreeNode(
    20, TreeNode(15, None, None), TreeNode(17, None, None)))
s = Solution()
s.levelOrder(node)
