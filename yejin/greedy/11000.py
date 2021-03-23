import sys
import heapq

N = int(sys.stdin.readline().rstrip())
classes = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().rstrip().split())
    classes.append((S, T))
classes.sort()

queue = []
heapq.heappush(queue, classes[0][1])

# 무조건 일찍 끝나는 강의실에 다음 강의 배정
for c in classes[1:N]:
    if c[0] < queue[0]:
        heapq.heappush(queue, c[1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, c[1])

print(len(queue))
