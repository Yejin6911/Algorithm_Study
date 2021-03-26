import abc
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
queue = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
rx, ry, bx, by = 0, 0, 0, 0
visited = [[[[False] * M for _ in range(N)]
            for _ in range(M)] for _ in range(N)]

# 처음 구슬 위치와 이동횟수를 1로 해서 queue에 넣어준다.
for i in range(N):
    row = list(sys.stdin.readline().rstrip())
    board.append(row)
    if 'R' in row:
        rx, ry = i, row.index('R')
    if 'B' in row:
        bx, by = i, row.index('B')
queue.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True


# 갈 수 있을 때까지 구슬 이동
def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


# 너비 우선 탐색
def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            # 파란색 구슬이 먼적 도착하지 않았을 때
            if board[nbx][nby] != 'O':
                # 빨간 구슬이 도착한 경우
                if board[nrx][nry] == 'O':
                    print(depth+1)
                    return
                # 같은 위치에 떨어지는 경우 이동거리가 많은 구슬을 한 칸 뒤로 옮긴다.
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # 방문하지 않은 위치면 queue에 넣어 준다.
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)
    return


bfs()
