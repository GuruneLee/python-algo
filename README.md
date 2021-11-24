# 코테 노트 (파이썬)
## python 문법 기초
### 정렬 라이브러리
- sorted, sort
    - sorted()
        - list, dict 등에 사용 가능
        - 반환결과는 항상 리스트
    - sort()
        - list 내장 함수
    - key = 함수() 사용 가능
    ~~~python
    arr = [9,8,0,1]
    # sorted
    result = sorted(arr)
    # sort
    arr.sort()
    ~~~

## 템플릿 template
### 재귀 깊이 설정
~~~python
import sys
sys.setrecursionlimit(10**6)
~~~

## String
### ASCII
- 'a'~'z' : 97~122
- 'A'~'Z' : 65~90
- '0'~'9' : 48~57
- ord(문자) => ASCII 십진수 출력
- chr(숫자) => 해당 문자 출력
### Case
- casefold
- upper?
- lower?
### 사전순 크기비료
- BA > BB - 문자가 큰게 더 큼
- AA > A - 크기가 다르고 비교가 불가능 하면 긴게 더 큼
- Aa > AAa - 크기가 다르면 앞에서부터 문자가 큰게 더 큼
- 관련 문제 - 백준 1294 문자열장식

## 중요 자료구조
### 트리
1. 이진 탐색 트리
- 트리 자료구조 중 가장 간단한 형태
- 이진 탐색이 동작할 수 있도록 고안된 자료구조
~~~python
# 이진탐색트리, BST
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
~~~

2. 서로소 집합 자료구조 (union-find)
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- parent 배열을 사용함
    - 초기엔 p\[i] = i 로 초기화 (자신이 자신의 부모 => 자신이 루트)
- 트리에서의 집합: root 가 같으면 한 집합 = 간선으로 연결되어있으면 한 집합
    - parent 배열을 사용하여 집합 표기
    - parent 배열에 각 부모를 저장해놔서 간선 연결 여부 파악하기
    - parent 배열을 이용해 root 같은지 판별하기
- 주어진 합집합 연산 처리 (union)
    - 트리에서의 합집합 연산: root 를 같게 하기
    - union(a,b): a의 루트 -\[간선]-> b의 루트
- 집합 찾기 ( = root 찾기) (find)
    - parent 배열에서 root 찾기
~~~python
# union-find 자료구조
## parent 배열
parent = [0]*(n+1)
## 특정 원소가 속한 집합(root) 찾기
def find_ver1(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
def find_ver2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
## 합집합 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        # 이 부분은... 문제에 따라 기준이 달라질 수 있음
        parent[b] = a
    else:
        parent[a] = b
~~~

## 중요 알고리즘 
### sort
1. 선택 정렬 O(n*n)
: 정렬이 안 된 숫자 중, 가장 작은 숫자를 선택해 앞으로 보내는 방식
~~~python
# 선택 정렬
for i in range(len(arr)):
    min_index = i; # 0부터 i-1까지는 절렬이 되어있는 상태임
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
        swap(arr[min_index], arr[j])
~~~

2. 삽입 정렬 O(n*n)
: 정렬이 안 된 숫자중 하나를 정렬이 된 숫자에 삽입하는 방식
~~~python
# 샵입 정렬
for i in range(len(arr)):
    for j in range(i, 1, -1):
        if arr[j] > arr[j-1]:
            swap(arr[j], arr[j-1])
        else:
            break
~~~

3. 퀵 정렬 O(nlogn)
- 분할 정복
- 기준 데이터(pivot)을 설정하고, 작은데이터와 큰데이터를 각각 한 곳에 몰아놓는다
~~~python
# 퀵 정렬
def quick_sort(start, end):
    if start>=end: return # 원소가 한 개인 경우
    
    pivot = start # 기준을 start로 하자 (어떻게 해도 상관은 x)
    left = start + 1
    reight = end
    while left<=right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            reight -= 1

        if left > right:
            # 엇갈렸다 -> 원하는 대로 위치를 다 바꿨다
            # => 따라서, 피벗을 요놈들 중간으로 옮기고 다음 단계로 가자
            swap(arr[right], arr[pivot])
            #  피벗이 right 인덱스로 오게 된다
        else:
            swap(arr[right], arr[left])
    quick_sort(start, right-1)
    quick_sort(right+1, end)
~~~
~~~python
# 퀵 정렬 - 파이써닉 한 방법
def quick_sort(array):
    if len(array)<=1: return array

    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
~~~

4. 계수 정렬 O(n+k) s.t. k는 데이터의 최대값
- 최소부터 최대까지 그 사이의 모든 수가 등장한 개수를 세고, 순차적으로 출력하기
- 매우 빠르지만, 특정한 조건에서만 사용가능
    - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때
    - 최대 최소 값의 차이가 1,000,000을 넘지 않을 때
~~~python
count = [0]*(max(arr)+1)
for i in range(len(arr)):
    count[arr[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
~~~

### Search
1. 이진 탐색 O(logn)
- 정렬된 데이터에서 원소를 찾는 탐색 알고리즘
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
- '시작' '끝' '중간' 변수 사용, 찾으려는 데이터와 '중간' 값을 계속 비교
~~~python
# 이진탐색 - 재귀
# target 의 위치 출력
arr.sort()
def binary_search(arr, target, start, end):
    if start > end: return None

    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
~~~
~~~python
# 이진탐색 - 반복문
# target 의 위치 출력
arr.sort()
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

~~~

### Shortest Path
1. 다익스트라 O(ElogV)
- 음의 간선이 없어야 한다 (사이클을 돌 가능성이 생김)
- 최단 거리 테이블 필요
~~~python
# 개선된 다익스트라 알고리즘
import heapq
INF = int(1e9)

# 노드의 개수, 간손의 개수
n, m = map(int, input().split(()))
# 시작 노드 번호
start = int(input())
# 그래프 정보
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
distance = [INF]*(n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
...
~~~
2. 플로이드 워셜 O(n^3)
- 현재 방문중인 노드를 제외한 N-1개의 노드 중, 서로 다른 노드 쌍 (A,B)를 선택한 후,
[A -> 현재방문노드 -> B] 의 비용을 확인해서 최단거리 갱신
- 모든 지점 간의 최단경로 구하기
- 2차원 배열 필요, DP 문제임
    - 점화식 : dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b]) 
~~~python
# 노드의 개수, 간손의 개수
n, m = map(int, input().split(()))
# 그래프 정보 (2차원 배열 / 인접행렬)
graph = [[INF]*(n+1) for _ in range(n+1)]
# 1. 자기자신에게 가는 비용은 0으로 초기화
# 2. 각 간선에 대한 정보를 받아, 그 값으로 초기화
# 3. 점화식에 따라, 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# 4. 출력
~~~
3. 벨만 포드
- 100% 이해는 못함
- 음수 사이클이 생기는지 판단할 수 있는 최소거리 알고리즘
- 프로세스
    1. 모든 간선마다
        - 간선이 잇는 출발 정점이 한번이라도 계산 된 정점 이라면(INF가 아니라면), 해당 간선이 잇는 정점의 거리를 비교해서 업데이트한다
        (Dist\[To] > Dist\[From] + cost(From, To) 이면 업데이트 함)
        - 단, 그래프가 끊어져 있다면,  INF 검사를 해야할 지 다시 생각해보자
    2. 1번 과정을 |V|-1번 반복한다
    3. 1번 과정을 한 번 더 반복한다
        - 업데이트가 발생하지 않는다 -> 출력
        - 업데이트가 발생한다 -> 음의 사이클 존재 (최소를 구할 수 없음)
- [도움받은 블로그](https://yabmoons.tistory.com/365)
~~~python
v, e
edges
dist = [INF]*(v+1)
def bellman_ford(start):
    dist[start] = 0
    for i in range(1, v): #v-1번 반복
        for edge in edges:
            From, To, cost = edge
            if dist[From] == INF: continue;
            if dist[To] > dist[From] + cost:
                dist[To] = dist[From] + cost
    for edge in edges:
            From, To, cost = edge
            if dist[From] == INF: continue;
            if dist[To] > dist[From] + cost:
                return False
    return True
## 최소 거리
print(min(dist))
~~~



### 그래프 이론
1. (union-find) 무방향 그래프 사이클 판별
- 각 간선을 확인하며 두 노드의 root를 확인한다
    - root가 서로 다르면 두 노드를 union 한다
    - root가 같다면 사이클 발생
~~~python
# 무방향 그래프 사이클 판별
v,e
parent

def isCycle(parent, v, e):
    for i in range(e):
        a,b
        if find(parent, a) == find(parent, b):
            return True
            break
        else:
            union(parent, a, b)
    return False
~~~
2. (union-find) 크루스칼 알고리즘
- 최소신장트리를 만드는 알고리즘
    - 신장트리: 그래프의 모든 노드를 포함하면서, 사이클이 존재하지 않는 부분 그래프
    - 최소신장트리: 간선의 합이 최소
- 프로세스
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬
    2. 모든 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
        - 사이클 발생하지 않음 -> 최소 신장 트리에 포함
        - 사이클 발생 -> 탈락
~~~python
# 크루스칼
v, e
parent
edges # [cost, a, b]
def kruskal(parent, edges):
    edges.sort()
    cost_sum = 0
    for edge in edges:
        cost, a, b = edge
        # 사이클 발생안할때만 집합에 포함
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            cost_sum += cost
    return cost_sum
## 최소신장트리
print(parent)
## cost
print(kruskal(parent, edges))
~~~

3. (union-find) 위상정렬 알고리즘
- 방향그래프의 모든 노드를 '방향을 거스르지 않도록 나열' 하는 알고리즘
    - ex. 선수과목을 고려한 학습 순서 결정
- 진입차수
    - 방향그래프 중, indegree 임 하아...
- 프로세스
    1. 진입차수가 0인 노드를 큐에 넣는다
    2. 큐가 빌 때까지 ...
        1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
        2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
~~~python
indegree
graph
v, e
def topology_sort():
    result = []
    q = dequeu()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return result

## 정렬 결과 출력
print(topology_sort)
~~~
### 정수론
1. 아라토스테네스의 체
- 소수 판별하는 알고리즘? 소수를 골라내는 알고리즘?

2. 두 수의 최대공약수 / 최소공배수
~~~python
# 최대공약수
def gcd(a, b):
    while b > 0:
        r = n % a
        a = b
        b = r
    return a

# 최소공배수
def lcm(a, b):
    g = gcd(a, b)
    return (a*b)//g
~~~

3. 조합, combination
- comb(n,r) = n!/r!(n-r)!
- comb(n,r) = comb(n-1, r-1) + comb(n-1, r)
~~~python
# 재귀
def comb(n, r):
    if n == r:
        return 1
    if r == 1:
        return n
    return comb(n-1, r-1) + comb(n-1, r)
~~~
~~~python
# 무식 - 팩토리얼 다 구하기
n, m = map(int, input().split())
fac = [1]*(n+1)
for i in range(1, n+1):
    fac[i] = fac[i-1]*i
print(fac[n]//(fac[m]*fac[n-m]))
~~~
4. 부분집합(power set) 구하기
- Binary Counting을 이용해보자
    - n번째 비트값이 1이면 n번째 원소가 포함되어있음을 의미
~~~ python
# 모든 부분집합을 출력하는 코드
arr = [1,2,3]
n = len(arr)
for i in range(1<<n): # 1<<n는 2**n 을 의미한다 ex.0001<<3 = 0100(8)
    for j in range(n):
        if i&(1<<j): # i의 j번째 비트가 1인지 아닌지 의미함
            print(arr[j], end=',')
~~~

### 문자열
1. 후위표기식
2. kmp
3. trie


### 분류 안됨
1. LIS
2. LCS
3. Knapsack, 배낭
4. 후위표기식
- 연산식 s
    - s[0] 부터 순서대로 훝으면서 ㄱㄱ
        1. 피연산자 그대로 출력
        2. 연산자는 
            1) 스택이 비어있다면 스택에 추가 
            2) 스택의 TOP이 자신보다 낮은 우선순위일 때 까지 pop 하고 추가
            * 단, 여는 괄호 '('는 닫는괄호가 아니면 pop하지 않음
        3. 닫는 괄호가 나오면 여는 괄호가 나올때까지 꺼내서 출력
        4. s[last]에 도착하면 스택에서 차례로 꺼내서 출력
        (ref: 백준 1918 후위 표기식)
~~~python
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
~~~
## 다시 풀어볼 문제
- 백준, 11660 (누적합)
- 백준, 편집거리
- 백준, LCS
