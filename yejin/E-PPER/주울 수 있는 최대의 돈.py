def solution(money):
    dp = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            dp[i] = money[i]
        elif i == 1:
            dp[i] = money[i-1]+money[i]
        elif i == 2:
            dp[i] = max(money[i-2]+money[i], money[i-1]+money[i], dp[i-1])
        else:
            dp[i] = max(dp[i-3]+money[i-1]+money[i], dp[i-2]+money[i], dp[i-1])
    return max(dp)


n = int(input())
# money = '[5, 7, 10, 1, 2, 10, 10, 8]'
money = input().strip()
money = list(map(int, money[1:len(money)-1].split(', ')))
print(solution(money))
