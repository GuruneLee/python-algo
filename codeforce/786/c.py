for _ in range(int(input())):
    s = input()
    t = input()

    if 'a' == t:
        print(1)
        continue
    if 'a' in t:
        print(-1)
        continue

    nofa = s.count('a')
    print(2**nofa)
