# 시간 복잡도 O(n*(n-1)*...*(n-m+1))

n, m = map(int,input().split())
visit = [-1 for _ in range(0, n+1)]
stack = []

l = []
def recurse(i): # STACK 의 i번째에 '숫자'를 넣는다.
    print(stack)
    if i==m:
        l.append(list(stack))
        return
    for num in range(1, n+1):
        if visit[num] == -1:
            stack.append(num)
            visit[num] = 1
            recurse(i+1)
            stack.pop()
            visit[num] = -1

recurse(0)

for e in l:
    for v in e:
        print(v, end=" ")
    print()