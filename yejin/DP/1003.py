import sys
input = sys.stdin.readline

t = int(input())
data = [int(input()) for _ in range(t)]

# 0,1 호출 횟수를 저장하는 리스트 각각 선언
dp_0 = [0 for _ in range(max(data)+1)]
dp_1 = [0 for _ in range(max(data)+1)]
dp_0[0], dp_1[1] = 1, 1

# 횟수 update
for i in range(2, max(data)+1):
    dp_0[i] = dp_0[i-1]+dp_0[i-2]
    dp_1[i] = dp_1[i-1]+dp_1[i-2]

for i in data:
    print(dp_0[i], dp_1[i])
