for _ in range(int(input())):
    s = input()

    f = s[0]
    ss = [f]
    for i in range(1, len(s)):
        if s[i] in ss:
            break
        ss.append(s[i])
        f = s[i]

    f = "".join(ss)
    # print(f)
    l = len(f)

    si = 0
    ei = 0
    flag = True

    while True:
        ei = si + l
        # print(si, ei)
        if si >= len(s):
            # print("index", si, ei)
            break
        if s[si:ei] != f:
            # print("not eq", si, ei, s[si:ei])
            flag = False
            break
        si += l

    # print(si, flag)
    if si < len(s) and not flag:
        # print("-")
        if f.startswith(s[si:]):
            flag = True

    if flag:
        print("yes")
    else:
        print("no")
