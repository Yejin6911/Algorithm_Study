import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
data = list(map(int, sys.stdin.readline().rstrip().split()))
operators = ['+']*data[0] + ['-']*data[1] + ['*']*data[2] + ['/']*data[3]

# 방법 1 - 순열 사용, set이용해서 중복 제거하여 시간초과 해결
steps = set(list(permutations(operators)))
# print(steps)
Max = -1000000001
Min = 1000000001

for step in steps:
    temp = numbers[0]
    for i in range(len(step)):
        if step[i] == '+':
            temp += numbers[i+1]
        elif step[i] == '-':
            temp -= numbers[i+1]
        elif step[i] == '*':
            temp *= numbers[i+1]
        else:
            temp = int(temp/numbers[i+1])
    Max = max(temp, Max)
    Min = min(temp, Min)

print(Max)
print(Min)


# 방법 2
def calculate(num, idx, add, sub, mul, div):
    global Max
    global Min
    if idx == n:
        Max = max(Max, num)
        Min = min(Min, num)
        return
    if add:
        calculate(num+numbers[idx], idx+1, add-1, sub, mul, div)
    if sub:
        calculate(num-numbers[idx], idx+1, add, sub-1, mul, div)
    if mul:
        calculate(num*numbers[idx], idx+1, add, sub, mul-1, div)
    if div:
        calculate(int(num/numbers[idx]), idx+1, add, sub, mul, div-1)


calculate(numbers[0], 1, data[0], data[1], data[2], data[3])
print(Max)
print(Min)
