import sys
sys.setrecursionlimit(10**5)

def sol(i, p, i_range, p_range):
    root = p[p_range[1]]
    print(root, end=" ")

    i_root_idx = i.index(root)

    i_left = (i_range[0], i_root_idx-1)
    i_right = (i_root_idx+1, i_range[1])

    left_len = i_root_idx - i_range[0]
    right_len = i_range[1] - i_root_idx

    p_left = (p_range[0], p_range[0]+left_len-1)
    p_right = (p_range[0]+left_len, p_range[1]-1)

    if left_len != 0:
        sol(i,p,i_left, p_left)
    if right_len != 0:
        sol(i,p,i_right, p_right)

from collections import deque

def s(i, p):
    q = deque()
    q.append(
        ((0,len(i)-1),(0, len(p)-1))
        )
    while q:
        i_range, p_range = q.popleft()
        root = p[p_range[1]]
        print(root, end=" ")
        
        i_root_idx = i.index(root)
        
        i_left = (i_range[0], i_root_idx-1)
        i_right = (i_root_idx+1, i_range[1])
        
        left_len = i_root_idx - i_range[0]
        right_len = i_range[1] - i_root_idx
        
        p_left = (p_range[0], p_range[0]+left_len-1)
        p_right = (p_range[0]+left_len, p_range[1]-1)
        
        if left_len != 0:
            q.append((i_left, p_left))
        if right_len != 0:
            q.append((i_right, p_right))
    

def sol1(i_range, p_range):
    root = p[p_range[1]]
    print(root, end=" ")

    i_root_idx = i.index(root)

    i_left = (i_range[0], i_root_idx-1)
    i_right = (i_root_idx+1, i_range[1])

    left_len = i_root_idx - i_range[0]
    right_len = i_range[1] - i_root_idx

    p_left = (p_range[0], p_range[0]+left_len-1)
    p_right = (p_range[0]+left_len, p_range[1]-1)

    if left_len != 0:
        sol1(i_left, p_left)
    if right_len != 0:
        sol1(i_right, p_right)

n = int(input())
i = list(map(int, input().split()))
p = list(map(int, input().split()))

# n = 6
# i = [i for i in range(100000, 0, -1)]
# p = [i for i in range(100000, 0, -1)]

sol1((0,n-1),(0,n-1))
# sol(i,p,(0,n-1),(0,n-1))
# print(i, p)
# s(i,p)
    
    
    