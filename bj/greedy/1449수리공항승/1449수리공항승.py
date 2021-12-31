n, l = map(int, input().split())
ll = list(map(int, input().split()))
ll.sort()

tape = 1
left = ll[0]
for i in range(len(ll)):
    if ll[i]-left+1 > l:
        left = ll[i]
        tape += 1
print(tape)
