import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y, board): # 외부 공기 0 -> -1
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    board[x][y] = -1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m):
                if(visited[nx][ny] == 0 and board[nx][ny] == 0):
                    visited[nx][ny] = 1
                    board[nx][ny] = -1
                    q.append([nx, ny])
    return board

def check(x, y, board): # 4면 중 외부 공기 개수 세기
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(board[nx][ny] == -1):
            cnt += 1
    return cnt

hour = 0
while(1):
    flag = 0
    temp = deepcopy(board)
    temp = bfs(0, 0, temp)
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1):
                flag = 1
                cnt = check(i, j, temp)
                if(cnt >= 2):
                    board[i][j] = 0
    if(flag == 1):
        hour += 1
    else:
        print(hour)
        break