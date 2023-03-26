# 용액
import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input()) # 100_000
l = list(map(int, input().split()))

i,j = 0,n-1
zero_arround = abs(l[i]+l[j])
zero_i, zero_j = 0,n-1
while i<j:
    if abs(l[i]+l[j]) < zero_arround:
        zero_arround = abs(l[i]+l[j])
        zero_i, zero_j = i, j
        
        if zero_arround == 0:
            break
    
    if l[i]+l[j] < 0:
        i += 1
    elif l[i]+l[j] >= 0:
        j -= 1
    

print(l[zero_i], l[zero_j])