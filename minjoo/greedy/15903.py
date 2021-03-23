import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
heapq.heapify(card)

cnt = 0
while(cnt < m):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    heapq.heappush(card, x+y)
    cnt += 1

print(sum(card))