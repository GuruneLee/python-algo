# def isLow(i, arr):
#     if i==len(arr)-1:
#         return arr[i-1]>arr[i]
#     return arr[i-1] > arr[i] and arr[i]<arr[i+1]
# def isHigh(i, arr):
#     if i==len(arr)-1:
#         return arr[i-1]<arr[i]
#     return arr[i-1] < arr[i] and arr[i] > arr[i+1]

# def do(arr, i, j, r): # i<j
#     a = 0
#     if 
#     for k in range(i, j+1):

# def car(stack, flag):
#     arr = [0]*len(stack)
#     for i in range(len(stack)-1):
#          if stack[i] < stack[i+1]:
#              arr[i+1] += 1

def candy(r):
    ans = 0
    stack = [r[0]]
    head = 1
    while stack[0]==r[head]:
        stack = [r[head]]
        head += 1
    head -= 1

    if head==len(r)-1:
        print(len(r))
        return
    print(head, stack)
    

candy([3,3,3,3,3,3,3,1])      
candy([1,0,2])
# print(candy([1,2,2]))
# print(candy([1,2,3,4,5,6]))
# print(candy([1,2,3,3,2,1]))