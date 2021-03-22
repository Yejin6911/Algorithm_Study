import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
nums = list(sys.stdin.readline().rstrip())

# 윽 시간초과
while K > 0:
    max_i = nums.index(max(nums))
    if max_i > 0:
        data = nums[:max_i]
    else:
        data = nums[max_i+1:]
    for _ in range(len(data)):
        Min = min(data)
        nums.remove(Min)
        K -= 1
        if K == 0:
            break

print(int(''.join(nums)))

# Stack이용
stack = []
k = K
for i in range(N):
    while stack and k > 0:
        if stack[-1] < nums[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(nums[i])

# K 빼주는 이유: 반복문 다 돌고 나서 k가 0이 아닌경우 고려
print(int(''.join(stack[:N-K])))
