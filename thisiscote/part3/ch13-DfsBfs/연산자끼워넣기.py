n = int(input())
l = list(map(int, input().split()))
op = list(map(int, input().split()))

tmp = []
test = []
candi = [int(1e9), -int(1e9)]
def dfs(idx, now):
    if idx==n-1:
        candi[0] = min(candi[0], now)
        candi[1] = max(candi[1], now)
        test.append((" ".join(tmp), now))
        return

    for i in range(4):
        if op[i] == 0: continue
        if i==0:
            op[i] -= 1
            tmp.append("+")
            dfs(idx+1, now+l[idx+1])
            tmp.pop()
            op[i] += 1
        if i==1:
            op[i] -= 1
            tmp.append("-")
            dfs(idx+1, now-l[idx+1])
            tmp.pop()
            op[i] += 1
        if i==2:
            op[i] -= 1
            tmp.append("*")
            dfs(idx+1, now*l[idx+1])
            tmp.pop()
            op[i] += 1
        if i==3:
            op[i] -= 1
            tmp.append("/")
            dfs(idx+1, now//l[idx+1] if now>=0 else -((-now)//l[idx+1]))
            tmp.pop()
            op[i] += 1

dfs(0, l[0])
# print(candi)
test.sort(key=lambda x: x[1])
for e in test:
    print(e)