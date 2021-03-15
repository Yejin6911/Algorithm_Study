import sys
import heapq

n = int(sys.stdin.readline().rstrip())
positive = []
negative = []
result = 0

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    # 1인경우 더하는게 결과값이 더 커지므로 result에 바로 더해준다
    if num == 1:
        result += 1
    # 양수인 경우 최대힙에 push
    elif num > 1:
        heapq.heappush(positive, (-num, num))
    # 음수나 0인 경우 최소힙에 push
    elif num <= 0:
        heapq.heappush(negative, num)

# 양수 최대값 두개씩 pop해서 곱한 후 결과 update
while len(positive):
    if len(positive) == 1:
        result += heapq.heappop(positive)[1]
    else:
        sum = heapq.heappop(positive)[1]*heapq.heappop(positive)[1]
        result += sum

# 음수 최소값 두개씩 pop해서 곱한 후 결과 update
# 0을 음수 배열에 포함시키는 이유: 0과 음수 곱하면 음수값 없어지므로 결과 값 더 크게 만들 수 있다.
while len(negative):
    if len(negative) == 1:
        result += heapq.heappop(negative)
    else:
        sum = heapq.heappop(negative)*heapq.heappop(negative)
        result += sum

print(result)
