# 문자열 사전 순
# BA > BB - 문자가 큰게 더 큼
# AA > A - 크기가 다르고 비교가 불가능 하면 긴게 더 큼
# Aa > AAa - 크기가 다르면 앞에서부터 문자가 큰게 더 큼
# 관련 문제 - 백준 1294 문자열장식

# ASCII 문자 유니코드


# 누적합 문제 - 이중 누적합
# 백준 11660
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

psum = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = psum[i+1][j] + l[i][j]
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j+1]


def asum(a, b, c, d):
    return psum[c][d]-psum[a-1][d]-psum[c][b-1]+psum[a-1][b-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(asum(x1, y1, x2, y2))

# union-find

parent = [i for i in range(n)]


def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# BST (이진 탐색 트리)
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
