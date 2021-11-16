# 1918 후위 표기식
priority = {
    '+':0,
    '-':0,
    '*':1,
    '/':1,
    '(':2
}
stack = []
s = input().rstrip()
for i in range(len(s)):
    if ord('A')<=ord(s[i])<=ord('Z'):
        print(s[i], end='')
    else:
        if s[i] == ')':
            while True:
                if stack[len(stack)-1] == '(':
                    break
                print(stack.pop(), end='')
            stack.pop()
        elif s[i] == '(':
            stack.append('(')
        else:
            while len(stack)>0 :
                if stack[len(stack)-1]=='(' or priority[stack[len(stack)-1]] < priority[s[i]]:#우선순위
                    break
                print(stack.pop(), end='')
            stack.append(s[i])
    # print(stack)
while len(stack) > 0:
    print(stack.pop(), end='')