import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]
dp[0] = stairs[0]
for i in range(1, n):
    if i == 1:
        dp[i] = stairs[i-1]+stairs[i]
    # min(1번계단+3번계단, 2번계단+3번계단)
    elif i == 2:
        dp[i] = max(stairs[i-1]+stairs[i], stairs[i-2]+stairs[i])
    # min(i-3번계단을 밟을 때의 최소 + i-1계단 + i계단, i-2번계단 밟을 떄의 최소 + i계단)
    else:
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[n-1])
