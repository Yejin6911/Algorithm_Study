import sys
input = sys.stdin.readline


def solution(num):
    dp = [0 for _ in range(n+1)]
    for i in range(2, num+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0 and dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
        if i % 2 == 0 and dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
    return dp[num]


n = int(input())
print(solution(n))
