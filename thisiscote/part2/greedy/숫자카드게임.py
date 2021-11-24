n, m = map(int,input().split())
MAX = 0
for _ in range(n)  :
    MAX = max(MAX, min(list(map(int, input().split()))))
print(MAX)
