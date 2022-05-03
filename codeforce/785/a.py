def f(s):
    score = 0
    for c in s:
        score += ord(c)-ord("a")+1
    return score


for _ in range(int(input())):
    s = input()
    if len(s) % 2 == 0:
        print("Alice", f(s))
    else:
        total = f(s)
        b = min(f(s[-1]), f(s[0]))
        a = total - b
        if a < b:
            print("Bob", b-a)
        else:
            print("Alice", a-b)
