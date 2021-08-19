import sys
input = sys.stdin.readline

t = int(input())
data = [int(input()) for _ in range(t)]
dp = [0 for _ in range(max(data)+1)]
for i in range(1, max(data)+1):
    if i == 1:
        dp[i] = dp[i-1]+1
    elif i == 2:
        dp[i] = dp[i-2]+dp[i-1]+1
    elif i == 3:
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]+1
    else:
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

for i in data:
    print(dp[i])
