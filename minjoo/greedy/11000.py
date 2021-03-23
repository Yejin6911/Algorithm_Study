# 어려워... 

import sys
import heapq

n = int(sys.stdin.readline()) # 수업의 개수
course = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    course.append([start, end])

course.sort(key = lambda x: x[0])
queue = []
heapq.heappush(queue, course[0][1]) # 맨 처음 강의 끝나는 시간

for i in range(1, n):
    if(queue[0] > course[i][0]): # 한 강의실 못쓰는 경우
        heapq.heappush(queue, course[i][1])
    else: # 한 강의실에서 이어서 강의 가능
        heapq.heappop(queue)
        heapq.heappush(queue, course[i][1]) # 끝나는 시간 교체

print(queue)    
print(len(queue))