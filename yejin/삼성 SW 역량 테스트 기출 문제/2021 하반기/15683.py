# PyPy3으로 제출. Python3 시간초과

import sys
import copy
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y, d):
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 더이상 체크 못하는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6:
            break
        # cctv이거나 이미 체크된 곳인 경우
        elif 1 <= visited[nx][ny] <= 5 or visited[nx][ny] == -1:
            x, y = nx, ny
        else:
            visited[nx][ny] = -1
            x, y = nx, ny


def dfs(dir):
    # cctv 방향 다 정해진 경우
    if len(dir) == len(cctv):
        global visited
        visited = copy.deepcopy(board)
        cnt = 0
        for i in range(len(cctv)):
            x = cctv[i][0]
            y = cctv[i][1]
            kind = board[x][y]
            if kind == 1:
                move(x, y, dir[i])
            elif kind == 2:
                move(x, y, dir[i])
                move(x, y, (dir[i]+2) % 4)
            elif kind == 3:
                move(x, y, dir[i])
                move(x, y, (dir[i] + 1) % 4)
            elif kind == 4:
                move(x, y, dir[i])
                move(x, y, (dir[i] + 1) % 4)
                move(x, y, (dir[i] + 2) % 4)
        cnt = 0
        for row in visited:
            cnt += row.count(0)
        global result
        result = min(result, cnt)
        return
    for i in range(4):
        dfs(dir+[i])


n, m = map(int, input().split())
board = []
cctv = []
cctv_5 = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] < 5:
            cctv.append((i, j))
        elif row[j] == 5:
            cctv_5.append((i, j))
    board.append(row)

# 5번만 먼저 처리
for c in cctv_5:
    x = c[0]
    y = c[1]
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = -1

result = sys.maxsize
dfs([])
print(result)
