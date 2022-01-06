t = int(input())
tc = []
for i in range(t):
    tc.append(int(input()))
def prime_list(x):
    sieve = [True]*x
    tt = int(x**0.5)
    for i in range(2, tt+1):
        if sieve[i]:
            for j in range(i+i, x, i):
                sieve[j] = False
    return [i for i in range(2,x) if sieve[i]==True ]

p = prime_list(max(tc))

for T in tc:
    l=T//2
    r=T-l
    while True:
        if l in p and r in p:
            print(l,r)
            break
        else:
            l-=1
            r+=1
