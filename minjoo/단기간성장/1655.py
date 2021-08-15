import sys, heapq

# max_heap : 최대 힙
# min_heap : 최소 힙
max_heap = []
min_heap = []

# ans : 정답 저장 배열
ans = []

# 수열의 갯수 입력
n = int(sys.stdin.readline())
for i in range(n):

    # 수열의 원소 입력
    m = int(sys.stdin.readline())
    
    # 같은 개수라면 무조건 최대힙으로 넣는다
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-1 * m,m))
        
    # 개수가 다르다는 것은 이전에 최대힙에 넣은 것이기 때문에
    # 개수를 맞춰주기 위해 최소힙에 넣는다
    else:
        heapq.heappush(min_heap, (m,m))
        
    # 앞에서 갯수 조건을 맞춰주었기에 대소 조건을 비교한다
    # 최소 힙의 top이 최대 힙의 top보다 작다면 두수를 바꿔준다 (최대 힙의 top이 중앙값이어야 하기 때문)
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp_min = heapq.heappop(min_heap)[1]
        temp_max = heapq.heappop(max_heap)[1]
        heapq.heappush(max_heap, (-1 * temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))
        
    # 갯수조건, 대소조건을 만족하였으니 최대 힙의 top이 중앙값이다
    ans.append(max_heap[0][1])

# 정답 출력
for i in ans:
    print(i)