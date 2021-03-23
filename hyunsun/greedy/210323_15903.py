
#카드정렬문제
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []
for card in cards:
    heapq.heappush(heap, card)

#for _ in range(n):
#    heapq.heappush(heap, int(input()))
    
for _ in range(m):
    x = heapq.heappop(heap) # 제일 작은 카드
    y = heapq.heappop(heap) # 두번째로 작은 카드
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)
    
print(sum(heap))
