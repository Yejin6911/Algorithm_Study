import heapq # 힙으로 구현
# 최솟값을 계속 찾아야 하는데 그때마다 sort하면 시간 복잡도가 너무 큼 
# 힙으로 구현하면 최솟값을 빠르게 찾을 수 있으며 새로운 원소를 push해도 자동으로 정렬된다

n = int(input()) # 숫자 카드 묶음 수
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

answer = 0
while(len(heap) > 1):
    temp1 = heapq.heappop(heap) # 제일 작은 카드
    temp2 = heapq.heappop(heap) # 두번째로 작은 카드
    temp = temp1 + temp2
    answer += temp
    heapq.heappush(heap, temp) 

print(answer)
