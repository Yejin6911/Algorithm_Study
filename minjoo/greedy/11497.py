import sys
import heapq

t = int(sys.stdin.readline()) # 테스트 케이스
for _ in range(t):
    n = int(sys.stdin.readline()) # 통나무 개수
    height = list(map(int, sys.stdin.readline().split())) # 통나무 높이
    heapq.heapify(height)

    rerange = [heapq.heappop(height)] # 최솟값부터 시작
    answer = 0 # 가장 큰 높이차
    while(height):
        rerange.insert(0, heapq.heappop(height))
        if(len(height) == 0):
            break
        rerange.append(heapq.heappop(height))
    
    for i in range(n):
        dif = abs(rerange[i-1]-rerange[i])
        if(dif > answer):
            answer = dif
    # print("답", rerange)
    print(answer)
