import heapq
import sys
input = sys.stdin.readline

# 방법!!!!
# https://art-coding3.tistory.com/44


left_heap = []  # 중앙값보다 작거나 같은 값, 최대힙 구성
right_heap = []  # 중앙값보다 큰 값, 최소힙 구성
answer = []

n = int(input())
for _ in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))

    # 갯수는 맞췄지만 왼쪽(최대 힙)의 루트가 오른쪽(최소 힙) 의 루트보다 큰 경우 둘이 바꿔준다.
    if right_heap and left_heap[0][1] > right_heap[0][0]:
        min = heapq.heappop(right_heap)[1]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))

    answer.append(left_heap[0][1])

for i in answer:
    print(i)
