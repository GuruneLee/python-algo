n = input()
le = len(n)-1

t = 9*le

for o in range(int(n)-t, int(n)):
    cal = o
    for k in str(o):
        cal += int(k)
    if cal == int(n):
        print(o)
        exit(0)
print(0)
