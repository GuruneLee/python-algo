# 시그마
## 못풀어서 다시 푸는문제
import sys
input=lambda:sys.stdin.readline().rstrip()

def mu(a, b):
    if b == 1:
        return a
    tmp = mu(a,b//2)
    if b%2 == 0:
        return tmp*tmp
    else:
        return tmp*tmp*a
        
m = int(input())
mod = 1000000007
ans = 0
for _ in range(m):
    b, a = map(int,input().split())
    ans += a*mu(b, mod-2) % mod
    ans = ans % mod

print(ans)