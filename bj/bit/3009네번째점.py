# XOR - 배타 합
# 같으면 0, 다르면 1
# 0^x == x
# x^x == 0
# 1^x == ~x
x = y = 0
for _ in range(3):
    tmp = list(map(int, input().split()))
    x ^= tmp[0]
    y ^= tmp[1]
print(x, y)
