import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split()) # 행, 열
board = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
oresult, vresult = 0, 0

def bfs(x, y):
    global oresult, vresult
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    ocnt, vcnt = 0, 0
    while(q):
        x, y = q.popleft()
        if(board[x][y] == 'o'):
            ocnt += 1
        elif(board[x][y] == 'v'):
            vcnt += 1
        else:
            pass

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<r and 0<=ny<c):
                if(visited[nx][ny] == 0 and board[nx][ny] != '#'):
                    visited[nx][ny] = 1
                    q.append([nx, ny])

    if(ocnt <= vcnt):
        vresult += vcnt
    else:
        oresult += ocnt

for i in range(r):
    for j in range(c):
        if(visited[i][j] == 0 and board[i][j] != '#'):
            bfs(i, j)

print(oresult, vresult)
