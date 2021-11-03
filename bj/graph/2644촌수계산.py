from queue import Queue
n = int(input())
a, b = list(map(int, input().split()))
m = int(input())
c = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    c[y].append(x)
    c[x].append(y)

q = Queue()
q.put(a)
v = [-1]*(n+1)
v[a] = 0
while not q.empty():
    cn = q.get()
    for nn in c[cn]:
        if v[nn] == -1:
            q.put(nn)
            v[nn] = v[cn]+1
        if nn == b:
            print(v[nn])
            exit(0)
print(-1)
