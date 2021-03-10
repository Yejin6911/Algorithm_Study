import sys

n = int(sys.stdin.readline().rstrip())
ropes = []
for i in range(n):
    rope = int(sys.stdin.readline().rstrip())
    ropes.append(rope)

# 내림차순으로 로프 정렬
ropes.sort(reverse=True)

# 최대 중량이 가장 큰 로프 한개만 이용했을 때
result = ropes[0]

# 그다음 중량부터 해당 로프를 포함할 때 들 수 있는 최대 무게 구해 현재 result와 비교
for i in range(1, len(ropes)):
    temp = ropes[i]*(i+1)
    result = max(temp, result)

print(result)
