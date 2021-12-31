s = input().split("-")

re = sum(map(int, s[0].split("+")))
for i in range(1, len(s)):
    re -= sum(map(int, s[i].split("+")))
    
print(re)
    