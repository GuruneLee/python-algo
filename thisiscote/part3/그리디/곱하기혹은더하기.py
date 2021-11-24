s = input()
l = int(s[0])
for i in range(1, len(s)):
    r = int(s[i])
    l = max(l+r, l*r)

print(l)

# solution
# 결론적으로 max 를 찾는게 맞긴 한데, 
# l또는r이 0또는1 일때는 무조건 더하기가 더 크고
# 아니면 곱하기가 무조건 더크다
