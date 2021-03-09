import sys
n = int(sys.stdin.readline().rstrip())

coins = [500, 100, 50, 10, 5, 1]
now = 0
result = 0
# 거스름돈 계산
left = 1000-n

# 동전 개수 계산
while now <= len(coins):
    if left == 0:
        break
    if left//coins[now] > 0:
        count = left//coins[now]
        left -= count*coins[now]
        result += count
    now += 1

print(result)
