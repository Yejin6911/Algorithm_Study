# 시간초과 개빡친다

n, k = map(int, input().split())
num = list(input())

cnt = 0
stack = [] # 정답

for i in range(n):
    while(stack and stack[-1] < num[i] and cnt < k):
        # stack의 마지막 원소가 더 작으면 삭제
        stack.pop()
        cnt += 1
    stack.append(num[i])

while(cnt < k): # 삭제할 횟수가 남았을 때
    stack.pop()
    cnt += 1

print(''.join(stack))
