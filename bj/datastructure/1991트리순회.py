# 출력보다 저장하는게 어려웠던 문제

n = int(input())

tl = {}
def pre(root):
    print(root, end='')
    if root in tl:
        if tl[root][0]!='.' : pre(tl[root][0])
        if tl[root][1]!='.' : pre(tl[root][1])
        
def inOrder(root):
    if root in tl and tl[root][0]!='.' : inOrder(tl[root][0])
    print(root, end='')
    if root in tl and tl[root][1]!='.' : inOrder(tl[root][1])

def postOrder(root):
    if root in tl and tl[root][0]!='.' : postOrder(tl[root][0])
    if root in tl and tl[root][1]!='.' : postOrder(tl[root][1])
    print(root, end='')
        
for _ in range(n):
    m,l,r = input().split()
    tl[m] = [l,r]

pre('A')
print()
inOrder('A')
print()
postOrder('A')
print()
    