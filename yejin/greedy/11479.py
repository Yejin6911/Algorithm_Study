import sys

T = int(sys.stdin.readline().rstrip())

# 방법 1
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    logs = list(map(int, sys.stdin.readline().rstrip().split()))
    logs.sort(reverse=True)
    Max, left, right = logs[0], logs[1], logs[2]
    level = max(Max-left, Max-right)
    # 가장 큰값을 가운데에 놓고 높은 통나무부터 왼쪽, 오른족 순서대로 하나씩 놓기
    for i in range(3, N):
        if i % 2:
            level = max(level, abs(left-logs[i]))
            left = logs[i]
        else:
            level = max(level, abs(right-logs[i]))
            right = logs[i]
    print(max(abs(right-left), level))


# 더 간단한 방법2 - 양쪽으로 하나씩 놓게 되면 인덱스 차이가 2만큼 날때마다의 차이를 비교해 주면 된다.
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    logs = list(map(int, sys.stdin.readline().rstrip().split()))
    logs.sort(reverse=True)
    level = 0

    for i in range(0, N-2):
        level = max(level, abs(logs[i] - logs[i+2]))
    print(level)
