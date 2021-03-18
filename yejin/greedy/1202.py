import sys
import heapq

N, K = map(int, sys.stdin.readline().rstrip().split())

D = []
for i in range(N):
    M, V = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(D, (M, V))

B = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
B.sort()

now = 0
result = 0

now_D = []
for b in B:
    while len(D) and b >= D[0][0]:
        # 현재 가방에 넣을 수 있는 보석들로 최대힙 구성
        heapq.heappush(now_D, -heapq.heappop(D)[1])
    if now_D:
        # 넣을 수 있는 보석중 가장 비싼 값을 결과에 더해준다.
        result += (-heapq.heappop(now_D))
    # 다음 가방에 넣을 수 있는 보석이 없을 때 break
    elif len(D) == 0:
        break

print(result)


# 시간초과 코드
# while True:
#     if now == len(B):
#         break
#     b = B[now]
#     d = heapq.heappop(D)
#     if d[1] <= b:
#         result += (-d[0])
#         now += 1
#     else:
#         heapq.heappush(D, d)
