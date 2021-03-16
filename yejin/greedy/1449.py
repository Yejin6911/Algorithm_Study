import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

# now : 현재 테이프가 커버할 수 있는 마지막 지점
now = 0
result = 0

for d in data:
    # 해당 지점을 넘어갔을 경우
    if now < d:
        # 새로운 테이프 붙이기
        result += 1
        now = d+L-1

print(result)
