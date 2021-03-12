import sys
import heapq

n = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# 시간초과 list에서 우선순위큐(heapq이용)로 변경하여 해결
heapq.heapify(cards)

result = 0
while len(cards) != 1:
    sum = heapq.heappop(cards)+heapq.heappop(cards)
    heapq.heappush(cards, sum)
    result += sum

print(result)
