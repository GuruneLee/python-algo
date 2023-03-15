# 문자열 폭발
## 23:10 ~ 23:54
DEFAULT_STR = "FRULA"

s = input()
f = input()

ans = []
for i in range(len(s)):
    ans.append(s[i])
    if len(ans) >= len(f) and ''.join(ans[-len(f):]) == f:
            del ans[-len(f):]
    

print(''.join(ans) if len(ans)>0 else DEFAULT_STR)