#https://level.goorm.io/exam/109218/13%ED%9A%8C-e-pper-9-%EC%A3%BC%EC%9A%B8-%EC%88%98-%EC%9E%88%EB%8A%94-%EC%B5%9C%EB%8C%80-%EB%8F%88/quiz/1
n = int(input())
money = list(map(int, input().split()))

dp = [0 for _ in range(n)]

if(n == 1):
    print(money[0])

elif(n == 2):
    print(money[0] + money[1])

else:
    dp[0] = money[0]
    dp[1] = money[0] + money[1]

    for i in range(2, n):
        if(i == 2):
            dp[i] = max(dp[i-1], money[i-1]+money[i], dp[i-2]+money[i])
            continue

        # 선택을 안하거나, i-1번째와 i를 선택하거나, i-1 선택안하고 i를 선택하는 것 중 최대값
        dp[i] = max(dp[i-1], dp[i-3]+money[i-1]+money[i], dp[i-2]+money[i])

    print(dp[n-1])