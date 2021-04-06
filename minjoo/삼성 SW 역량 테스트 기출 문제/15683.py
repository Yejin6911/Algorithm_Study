import sys
import math
from collections import deque
import copy
input = sys.stdin.readline
INF = sys.maxsize

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] #서동북남
di = [0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[1,2],[1,3],[0,2],[0,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]

MIN = INF
def dfs(start, MAP, cctv):
    global MIN
    if(start == len(cctv)): # CCTV 방향 다 정하면
        cnt = 0
        for x in range(n):
            for y in range(m):
                if(MAP[x][y] == 0): # 사각지대 세기
                    cnt += 1
        MIN = min(MIN, cnt)
        return
    
    num, x, y = cctv[start] # CCTV 방향, X좌표, Y좌표
    for d in di[num]:
        temp = copy.deepcopy(MAP)
        for i in d:
            nx = x + dx[i]
            ny = y + dy[i]
            while(0<=nx<n and 0<=ny<m): # 범위체크
                if(temp[nx][ny] == 6): # 벽이면 멈춤
                    break
                elif(temp[nx][ny] == 0): # 빈칸이면
                    temp[nx][ny] = '#'
                nx += dx[i] 
                ny += dy[i]
        dfs(start+1, temp, cctv)


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for x in range(n):
    for y in range(m):
        if(room[x][y] not in [0, 6]):
            cctv.append([room[x][y], x, y]) # cctv종류, x좌표, y좌표

dfs(0, room, cctv) 
print(MIN)