import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

# key idea: dp(n) = min(dp(n//3)+1, dp(n//2)+1, dp(n-1)+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if(i % 2 == 0 and dp[i] > dp[i//2] + 1):
        dp[i] = dp[i//2] + 1

    if(i % 3 == 0  and dp[i] > dp[i//3] + 1):
        dp[i] = dp[i//3] + 1

print(dp[n])