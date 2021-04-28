import sys
from collections import deque
input = sys.stdin.readline

n, m, oil = map(int, input().split()) # 격자 크기, 승객수, 초기 연료
board = [list(map(int, input().split())) for _ in range(n)]
driver_x, driver_y = map(int, input().split()) # 운전을 시작하는 위치
passenger_start = []
passenger_end = []
for i in range(m):
    line = list(map(int, input().split()))
    passenger_start.append([line[0]-1, line[1]-1])
    passenger_end.append([line[2]-1, line[3]-1])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    if([x, y] in passenger_start):
        return x, y, 0
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append([x, y])
    cand = []
    oil_cnt = 0
    while(q):
        temp = []
        oil_cnt += 1
        while(q):
            x, y = q.pop(0)
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and board[nx][ny] != 1):
                    visited[nx][ny] = 1
                    if([nx, ny] in passenger_start):
                        cand.append([nx, ny])
                    else:
                        temp.append([nx, ny])
        if(cand): # 승객 태울 후보가 있으면
            cand.sort(key = lambda x:(x[0], x[1]))
            return cand[0][0], cand[0][1], oil_cnt
        q = q + temp
    return -1, -1, -1 # 못간다

def goend(x, y, end_x, end_y):
    oil_cnt = 0
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([x, y])
    while(q):
        temp = deque()
        oil_cnt += 1
        while(q):
            x, y = q.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and board[nx][ny] != 1):
                    visited[nx][ny] = 1
                    if([nx, ny] == [end_x, end_y]):
                        return oil_cnt
                    temp.append([nx, ny])
        q = q + temp
    return -1

driver_x -= 1
driver_y -= 1
while(passenger_start):
    nx, ny, oil_cnt = bfs(driver_x, driver_y)
    if(nx == -1 or oil < oil_cnt):
        oil = -1
        break
    oil -= oil_cnt # 연료 소진
    idx = passenger_start.index([nx, ny]) # 태운 손님 번호
    passenger_start.pop(idx)
    end_x, end_y = passenger_end.pop(idx) # 태운 손님 목적지
    oil_cnt2 = goend(nx, ny, end_x, end_y)
    if(oil_cnt2 == -1 or oil < oil_cnt2):
        oil = -1
        break
    oil -= oil_cnt2 # 연료 소진
    oil += oil_cnt2 * 2 # 연료 충전
    driver_x, driver_y = end_x, end_y


print(oil)