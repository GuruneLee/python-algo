from queue import Queue

s = int(input())

q = Queue()
dp = [[-1]*2001 for _ in range(2001)]
q.put([1, 0, 0])
while not q.empty():
    cnum, ctime, cb = q.get()
    if cnum == s:
        print(ctime)
        exit(0)
    # 붙여넣기
    if cb != 0 and cnum+cb < s*2 and dp[cnum+cb][cb] == -1:
        q.put([cnum+cb, ctime+1, cb])
        dp[cnum+cb][cb] = 1
    # 하나 제거
    if cnum != 0 and dp[cnum-1][cb] == -1:
        q.put([cnum-1, ctime+1, cb])
        dp[cnum-1][cb] = 1
    # 복사
    if cnum < s*2 and dp[cnum][cnum] == -1:
        q.put([cnum, ctime+1, cnum])
        dp[cnum][cnum] = 1

print(0)
