import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]


def func(w):
    print(w.find)
    l = [0]*100
    l[ord(w[0])-97] += 1
    for i in range(1, len(w)):
        p = ord(w[i-1])-97
        c = ord(w[i])-97
        if (p != c) and l[c] != 0:
            return False
        l[c] += 1
    return True


count = 0
for i in range(n):
    if func(words[i]):
        count += 1

print(count)
