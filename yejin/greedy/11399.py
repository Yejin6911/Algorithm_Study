import sys

n = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split()))

people.sort()

# 방법 1 - 해당 사람이 걸리는 시간을 result에 계속 더해준다.
result = 0
for i in range(n):
    time = sum(people[:i+1])
    result += time

print(result)

# 방법 2 - 해당 사람의 시간을 더해야 하는 횟수만큼 곱해 result에 계속 더해준다.
count = n
result = 0
for i in range(n):
    result += time[i]*count
    count -= 1

print(result)
