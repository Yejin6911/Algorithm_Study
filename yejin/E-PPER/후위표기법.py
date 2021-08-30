m = int(input())
data = list(input().split())

stack = []
for i in data:
    if i.isdigit():
        stack.append(i)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(b-a)
        elif i == '/':
            stack.append(int(b/a))
        else:
            stack.append(a*b)
print(stack[-1])
