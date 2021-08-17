import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[0] = 1
    for i in range(2, n+1):
        if(i - 1 >= 0):
            dp[i] += dp[i-1] # i-1에서 1더하는 방법
        if(i - 2 >= 0):
            dp[i] += dp[i-2] # i-2에서 2더하는 방법
        if(i - 3 >= 0):
            dp[i] += dp[i-3] # i-3에서 3더하는 방법

    print(dp[n])