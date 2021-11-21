s = input()

cx = int(s[1])-1
cy = ord(s[0])-ord('a')

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

count = 0
for i in range(8):
    nx = cx+dx[i]
    ny = cy+dy[i]
    if 0<=nx<8 and 0<=ny<8:
        count += 1
print(count)