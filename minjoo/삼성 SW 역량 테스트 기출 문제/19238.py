import sys
from collections import deque
input = sys.stdin.readline

n, m, oil = map(int, input().split()) # 영역크기, 손님 수, 연료 양
board = [list(map(int, input().split())) for _ in range(n)] # 지도

x, y = map(int, input().split())
x, y = x-1, y-1 # 운전을 시작하는 칸

start, end = [], [] # 출발지, 목적지
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    start.append([start_x-1, start_y-1])
    end.append([end_x-1, end_y-1])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    dis = 0
    if([x, y] in start):
        return x, y, dis
    q = []
    q.append([x, y])
    cand = []
    while(q):
        temp = []
        dis += 1
        while(q):
            x, y = q.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n and board[nx][ny] == 0 and visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    if([nx, ny] in start):
                        cand.append([nx, ny])
                    else:
                        temp.append([nx, ny])
        if(cand):
            cand.sort(key = lambda x:(x[0], x[1]))
            return cand[0][0], cand[0][1], dis
        q = q + temp
    return -1, -1, -1
 
def gotoend(x, y):
    visited = [[0]*n for _ in range(n)]
    dis = 0

    idx = start.index([x, y]) # 승객 번호
    end_x, end_y = end[idx] # 목적지
    q = []
    q.append([x, y])
    while(q):
        dis += 1
        temp = []
        while(q):
            x, y = q.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n and board[nx][ny] == 0 and visited[nx][ny] == 0):
                    if([nx, ny] == [end_x, end_y]):
                        return dis
                    visited[nx][ny] = 1
                    temp.append([nx, ny])
        q += temp
    return -1

cnt = 0 # 이동 완료한 승객 수
while(cnt < m):
    x, y, dis = bfs(x, y) # 승객 태우러 감
    if(x == -1): # 승객 태우러 못감 (길이막힘)
        oil = -1
        break
    oil -= dis # 이동 거리만큼 연료 소진
    if(oil < 0): 
        oil = -1
        break # 이동할 수 없음

    dis = gotoend(x, y) # 목적지로
    if(dis == -1):
        oil = -1
        break
    oil -= dis # 이동 거리만큼 연료 소진
    if(oil < 0):
        oil = -1
        break # 이동할 수 없음
    oil += (dis*2) # 연료 충전

    cnt += 1
    idx = start.index([x, y])
    x, y = end[idx]
    start.pop(idx)
    end.pop(idx)
    
print(oil)