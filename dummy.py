s = input()
s2 = ""
digit = ["000", "001", "010", "011", "100", "101", "110", "111"]
print(int(digit[int(s[0])]), end="")
for i in range(1,len(s)):
    print(digit[int(s[i])], end="")
print()