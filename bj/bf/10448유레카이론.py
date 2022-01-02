# 참고로 i 번째 삼각수는 i(i+1)/2 이다.
# 즉, 아래처럼 안해도 된다.
# 난 바볼까?

t = []
cur = 0
plus = 1
while cur < 1000:
    cur += plus
    t.append(cur)
    plus += 1

for _ in range(int(input())):
    k = int(input())
    flag = False
    for a in t:
        for b in t:
            for c in t:
                if a+b+c==k:
                    print(1)
                    flag = True
                if flag: break
            if flag: break
        if flag: break
    if not flag:
        print(0)