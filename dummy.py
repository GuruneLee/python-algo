# 5639

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def post(self):
        def _post(root):
            if root is None:
                pass
            else:
                _post(root.left)
                _post(root.right)
                print(root.data)
        _post(self.root)


# 전위 -> 후위로 결과 바꾸기
bst = BST()
while True:
    try:
        bst.insert(int(input()))
    except:
        break
bst.post()
