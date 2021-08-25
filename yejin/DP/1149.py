import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # i번째 빨간색+{(i-1)번째가 초록색일때의 최소값과 (i-1)번째가 파란색일 때의 최솟값 중 최솟값}
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    # i번째 초록색+{(i-1)번째가 빨간색일때의 최소값과 (i-1)번째가 파란색일 때의 최솟값 중 최솟값}
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    # i번째 파란색+{(i-1)번째가 빨간색일때의 최소값과 (i-1)번째가 초록색일 때의 최솟값 중 최솟값}
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[n-1]))
