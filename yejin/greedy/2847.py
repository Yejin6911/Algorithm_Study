import sys

N = int(sys.stdin.readline().rstrip())
scores = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

M = scores[-1]
result = 0

for i in range(len(scores)-2, -1, -1):
    # 앞의 점수가 더 큰경우
    if scores[i] >= M:
        result += (scores[i]-(M-1))
        # 바로 레벨 점수-1 로 변경
        scores[i] = M-1
        M = scores[i]
    else:
        M = scores[i]

print(result)
