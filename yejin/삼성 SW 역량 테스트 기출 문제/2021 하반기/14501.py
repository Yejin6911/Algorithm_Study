import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

if data[n-1][0] == 1:
    dp[n-1] = data[n-1][1]
for i in range(n-2, -1, -1):
    # 해당일 상담이 가능한 경우
    if i+data[i][0] <= n:
        # 해당일에 시작하는 상담을 한 경우 vs 안한경우
        dp[i] = max(dp[i+1], data[i][1]+dp[i+data[i][0]])
    # 불가능한 경우
    else:
        dp[i] = dp[i+1]

print(dp[0])
