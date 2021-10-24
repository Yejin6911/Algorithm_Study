import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 공간의 크기
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
board = []
shark_x, shark_y = 0, 0 # 아기상어 위치
shark = 2 # 아기상어 크기
eat_cnt = 0 # 먹은 물고기 수
sec = 0 # 흐른 시간
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if(line[j] == 9):
            shark_x, shark_y = i, j
    board.append(line)

def bfs(x, y, b):
    global shark, eat_cnt # 아기상어 크기, 먹은 물고기 수
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append([x, y])
    visited[x][y] = 1
    b[x][y] = 0
    eat = []
    s = 0
    while(q):
        temp = []
        s += 1
        while(q):
            x, y = q.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n and b[nx][ny] <= shark and visited[nx][ny] == 0):
                    if(b[nx][ny] < shark and b[nx][ny] != 0):
                        eat.append([nx, ny]) # 물고기좌표 x, y, 물고기 크기
                    temp.append([nx, ny])
                    visited[nx][ny] = 1
        if(len(eat) > 0): # 먹을 물고기 후보가 있으면
            eat.sort(key=lambda z:(z[0], z[1]))
            b[eat[0][0]][eat[0][1]] = 0 # 물고기 먹음
            x, y = eat[0][0], eat[0][1]
            eat_cnt += 1
            if(eat_cnt == shark):
                shark += 1 # 아기상어 크기 1 증가
                eat_cnt = 0 # 카운트 초기화
            return x, y, b, s
        q = q + temp
    return -1, -1, -1, -1


while(1):
    shark_x, shark_y, board, s = bfs(shark_x, shark_y, board)
    if(shark_x == -1):
        print(sec)
        break
    else:
        sec += s