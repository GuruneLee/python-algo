# 16953 A에서B
from queue import Queue

a, b = input().split()

dp = {}
dp[a] = 0
q = Queue()
q.put(a)

while not q.empty():
    cs = q.get()
    ns = cs + '1'
    if ns == b:
        print(dp[cs]+2)
        exit(0)
    if int(ns) < int(b):
        if ns not in dp:
            dp[ns] = dp[cs]+1
            q.put(ns)
    ns = str(int(cs)*2)
    if ns == b:
        print(dp[cs]+2)
        exit(0)
    if int(ns) < int(b):
        if ns not in dp:
            dp[ns] = dp[cs]+1
            q.put(ns)
print(-1)
