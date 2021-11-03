for _ in range(int(input())):
    k = input().rstrip()
    s = input().rstrip()
    sum = 0
    for i in range(1, len(s)):
        sum += abs(k.index(s[i]) - k.index(s[i-1]))
    print(sum)
