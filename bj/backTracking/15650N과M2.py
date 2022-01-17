# 시간 복잡도 O()

import time

n, m = map(int,input().split())
stack = []

l = []
def recurse(i, k): # STACK 의 i번째에 '숫자'를 넣는다.
    if i==m:
        for i in range(0, m):
            print(stack[i], end=" ")
        print()
        return
    for num in range(1, n+1):
        if num > k:
            stack.append(num)
            recurse(i+1, num)
            stack.pop()

start = time.time()
recurse(0,0)
end = time.time()
print(f"{end - start:.5f} sec")

# for e in l:
#     for v in e:
#         print(v, end=" ")
#     print()