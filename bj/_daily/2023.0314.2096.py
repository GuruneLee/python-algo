# 내려가기
import sys
input=lambda:sys.stdin.readline().rstrip()

max_ = [0,0,0]
min_ = [0,0,0]
a,b,c = 0,0,0
x1,x2,x3 = 0,0,0
y1,y2,y3 = 0,0,0

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    x1,x2,x3 = max(a+max_[0], a+max_[1]), max(b+max_[0], b+max_[1], b+max_[2]), max(c+max_[1], c+max_[2])
    y1,y2,y3 = min(a+min_[0], a+min_[1]), min(b+min_[0], b+min_[1], b+min_[2]), min(c+min_[1], c+min_[2])
    
    max_[0], max_[1], max_[2] = x1,x2,x3
    min_[0], min_[1], min_[2] = y1,y2,y3

print(max(max_), min(min_))