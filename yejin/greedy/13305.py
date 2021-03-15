import sys
import heapq

# 우선 맞추긴 했는데...너무 볶잡하게 풀었다
N = int(sys.stdin.readline().rstrip())
R = list(map(int, sys.stdin.readline().rstrip().split()))

C = list(map(int, sys.stdin.readline().rstrip().split()))
# 의미없는 마지막 주유소 가격 제거
C.pop(-1)

for i in range(len(C)):
    # 도시 순서와 함께 다시 튜플 형태로 저장
    C[i] = (C[i], i)
heapq.heapify(C)

# 방문 여부 저장 리스트, 마지막 도시는 이미 방문한 것으로 표시
visited = [False for _ in range(N)]
visited[-1] = True

result = 0
while len(C):
    # 값이 가장 작은 도시를 pop해서 방문처리 및 해당 금액으로 갈 수 가장 먼 도시를 찾아 (거리 * 금액) 계산 후 결과값에 더해준다.
    now = heapq.heappop(C)
    if visited[now[1]] == True:
        continue
    for i in range(now[1]+1, N):
        # 중간에 있는 도시들도 방문 처리
        if visited[i] == False:
            visited[i] = True
        else:
            result += (sum(R[now[1]:i])*now[0])
            break
    # 해당 도시 방문 처리
    visited[now[1]] = True

print(result)

# 너무나도 간단한 두번째 풀이 ^^...
N = int(sys.stdin.readline().rstrip())
R = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
m = C[0]
for i in range(N-1):
    # 이전 도시까지의 최소 비용보다 더 비용이 작은 경우 최솟값 update
    m = min(m, C[i])
    result += m*R[i]

print(result)
