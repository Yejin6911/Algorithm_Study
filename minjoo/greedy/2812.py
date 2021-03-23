# 시간초과 개빡친다

n, k = map(int, input().split())
num = list(input())

cnt = 0
stack = []
answer = ''

for i in range(n):
    while(stack and stack[-1] < num[i] and cnt < k):
        stack.pop()
        cnt += 1
    stack.append(num[i])

while(cnt < k):
    stack.pop()
    cnt += 1

print(''.join(stack))
