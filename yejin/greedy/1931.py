import sys
n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    data.append((start, end))

# 시작 시간 순으로 먼저 정렬 후 끝나는 시간 기준으로 정렬
data.sort()
data.sort(key=lambda time: time[1])

result = 1
end = data[0][1]

for i in range(1, n):
    if data[i][0] >= end:
        result += 1
        end = data[i][1]

print(result)
