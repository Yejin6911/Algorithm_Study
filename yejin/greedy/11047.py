import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
prices = []

for i in range(n):
    price = int(sys.stdin.readline().rstrip())
    prices.append(price)

# 동전을 내림차순으로 정렬
prices.sort(reverse=True)

result = 0
# 금액이 가장 큰 동전부터 사용할 수 있는 최대 개수를 구해 result에 더해준다.
for i in range(n):
    if prices[i] <= k:
        num = k//prices[i]
        result += num
        k = k-prices[i]*num

print(result)
