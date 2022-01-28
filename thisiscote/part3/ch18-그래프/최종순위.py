# 19:37 - 19:58
from collections import deque

def topology_sort(indegree, graph, n):
    result = []
    q = deque()

    for i in range(1, n+1):
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

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    indegree = [0]*(n+1)
    # grade[i] 에 j 가 포함됨 (i -간선-> j)
    grade = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            grade[l[j]].append(l[i])
            indegree[l[i]] += 1
    
    m = int(input())
    for i in range(m):
        a, b = map(int,input().split())
        if b in grade[a]:
            grade[a].remove(b)
            grade[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            grade[b].remove(a)
            grade[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    
    ts = topology_sort(indegree, grade, n)
    if len(ts) < n:
        print("IMPOSSIBLE")
    else:
        print(
            " ".join(map(str, reversed(ts)))
        )
    
    