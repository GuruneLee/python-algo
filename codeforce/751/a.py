import sys
input = sys.stdin.readline

t = int(input())
ss = list(input().rstrip() for _ in range(t))
for s in ss:

    if s[0] != s[len(s)-1]:
        tmp = s[0:len(s)-1] + s[0]
    else:
        tmp = s
    print(tmp)
