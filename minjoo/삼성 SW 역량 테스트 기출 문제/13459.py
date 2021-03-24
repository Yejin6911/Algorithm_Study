import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

q = deque()

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 'R'):
                rx, ry = i, j
            elif(board[i][j] == 'B'):
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    count = 0
    while(board[x+dx][y+dy] != '#' and board[x][y] != 'O'):
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if(depth > 10):
            print(0)
            return

        for i in range(4):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if(board[next_bx][next_by] == 'O'):
                continue
            if(board[next_rx][next_ry] == 'O'):
                print(1)
                return

            if(next_rx == next_bx and next_ry == next_by):
                if(r_count > b_count):
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1))
    print(0)

bfs()
