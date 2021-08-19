import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    dp = [[0, 0] for _ in range(n+1)]

    # print(dp)
    dp[0] = [1, 0]
    if(n >= 1):
        dp[1] = [0, 1]

    if(n >= 2):
        for i in range(2, n+1):
            dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

    print(*dp[n])