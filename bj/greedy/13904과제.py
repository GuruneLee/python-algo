n = int(input())
dw = [list(map(int, input().split())) for _ in range(n)]
dw.sort(key=lambda x: (x[0], -x[1]))

greedy = []
for i in range(n):
    d, w = dw[i]
    greedy.sort()
    if len(greedy) < d:
        greedy.append(w)
    else:
        greedy[0] = greedy[0] if greedy[0] > w else w


print(sum(greedy))


# 1 20
# 2 50
# 3 30
# 4 10
# 4 40
# 4 60
# 6 5

# 4 60
# 2 50
# 4 40
# 3 30
# 1 20
# 4 10
# 6 5
