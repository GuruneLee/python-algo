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
    
# 후위표기식 - 스택 이용
## s[0] 부터 순서대로 훝으면서 ㄱㄱ
## 1. 피연산자 그대로 출력
## 2. 연산자는 
### 1) 스택이 비어있다면 스택에 추가 
### 2) 스택의 TOP이 자신보다 낮은 우선순위일 때 까지 pop 하고 추가
### * 단, 여는 괄호 '('는 닫는괄호가 아니면 pop하지 않음
## 3. 닫는 괄호가 나오면 여는 괄호가 나올때까지 꺼내서 출력
## 4. s[last]에 도착하면 스택에서 차례로 꺼내서 출력
# ref: 백준 1918 후위 표기식
stack = []
s = "A+B/C*D*(E+F)"
for i in range(len(s)):
    if ord('A')<=ord(s[i])<=ord('Z'):
        print(s[i])
    else:
        if s[i] == ')':
            while True:
                if stack[len(stack)-1] == '(':
                    break
                print(stack.pop())
            stack.pop()
        else:
            while len(stack)>0 :
                if stack[len(stack)] < s[i]:#우선순위
                    break
                print(stack.pop())
            stack.append(s[i])

# 부분집합(power set)
## 1) 중첩 for문
## 2) Binary Counting * - n번째 비트값이 1이면 n번째 원소가 포함되어있음을 의미
## 모든 부분집합을 출력하는 코드
arr = [1,2,3]
n = len(arr)
for i in range(1<<n): # 1<<n는 2**n 을 의미한다 ex.0001<<3 = 0100(8)
    for j in range(n):
        if i&(1<<j): # i의 j번째 비트가 1인지 아닌지 의미함
            print(arr[j], end=',')

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
