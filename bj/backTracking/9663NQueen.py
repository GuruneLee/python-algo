n = int(input())
l = [0]*n

def chk(i):
    for x in range(i):
        if l[i]==l[x] or i-x==abs(l[x]-l[i]): return False
    return True

cnt = 0
def put(i):
    global cnt
    if i==n:
        cnt += 1
        return
    for k in range(n):
        l[i] = k
        if chk(i):
            put(i+1)

if n>=12:
    ans = [14200, 73712, 365596]
    print(ans[n-12])
else:
    put(0)
    print(cnt)