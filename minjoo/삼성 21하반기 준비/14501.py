import sys
input = sys.stdin.readline

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
tp.insert(0, [0, 0])

ans = 0
def dfs(money, day):
    global ans, n
    if(day >= n):
        if(day == n and tp[day][0] == 1):
            money += tp[day][1]
        ans = max(ans, money)
        return

    t = tp[day][0]
    p = tp[day][1]

    next_day = day + t
    if(next_day <= n + 1):
        next_money = money + p
        dfs(next_money, next_day)
        
    dfs(money, day + 1)

dfs(0, 1)
print(ans)