from abc import abstractclassmethod


m = int(input())
line = list(input().split())

stack = []
op = ['+', '-', '*', '/']
flag = 0
ans = 0

for i in range(m):
    if(line[i] not in op): # 숫자일 경우
        stack.append(int(line[i]))
    else:
     
        b = stack.pop()
        a = stack.pop()
        
        if(line[i] == '+'):
            ans = a + b
        elif(line[i] == '-'):
            ans = a - b
        elif(line[i] == '*'):
            ans = a * b
        else:
            ans = a // b

        stack.append(ans)

    

print(stack[0])
