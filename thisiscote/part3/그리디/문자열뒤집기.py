s = input()
c = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        c += 1
if c==0:
    print(0)
else:
    if s[0]==s[len(s)-1]:
        print(c//2)
    else:
        print(c//2+1)
        
# official
# 앞에서부터 차례대로 순회하며, 전부 0으로 바꾸는 경우와 1로 바꾸는 경우를
# 각각 세서 계산하는 방식으로 소개되어있다.
# 근데 내 방법이 더 나은듯.
# 난 처음부터 더 적은걸 세서 문제를 풀었다