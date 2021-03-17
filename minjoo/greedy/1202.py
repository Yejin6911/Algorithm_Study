import sys
import heapq

n, k = map(int, input().split()) # 보석의 개수, 가방의 개수
wv = [] # 보석의 무게, 가격
bag = [] # 가방에 담을 수 있는 최대 무게
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    heapq.heappush(wv, [w, v])
for _ in range(k):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)

wvheap = [] # 현재 가방의 capacity보다 작은 모든 보석들
answer = 0

for _ in range(k):
    capacity = heapq.heappop(bag) # 가장 작은 bag
    while(wv and capacity >= wv[0][0]): # capacity보다 가벼운 모든 보석
        [w, v] = heapq.heappop(wv)
        heapq.heappush(wvheap, -v)

    if(wvheap):
        answer -= heapq.heappop(wvheap) # 가장 비싼 보석 pop
    elif(not wv): # 남은 보석이 없는 경우
        break

print(answer)




# answer = 0
# for i in range(k):
#     maxv = 0
#     idx = 0
#     while(mv[idx][0] <= bag[i]):
#         if(maxv < mv[idx][1]):
#             maxv = mv[idx][1]
#         idx += 1
#         if(idx == len(mv)):
#             break
#     mv.pop(idx-1)
#     answer += maxv

# print(answer)