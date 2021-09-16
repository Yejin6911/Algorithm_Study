from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, d):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while board[x+dx[d]][y+dy[d]] != '#' and board[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt


# Main
n, m = map(int, input().split())
board = []
red = (0, 0)
blue = (0, 0)
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = list(input().rstrip())
    if 1 <= i < n-1:
        for j in range(1, m-1):
            if row[j] == 'R':
                rx, ry = i, j
            elif row[j] == 'B':
                bx, by = i, j
    board.append(row)

queue = deque()
queue.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = 1

while queue:
    rx, ry, bx, by, cnt = queue.popleft()
    if cnt >= 10:
        break
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, i)
        nbx, nby, bcnt = move(bx, by, i)

        if board[nbx][nby] != 'O':
            # 빨간색이 먼저 구멍에 도착한 경우
            if board[nrx][nry] == 'O':
                print(cnt+1)
                sys.exit(0)
            # ***서로 겹친 경우 -> 이동 횟수 더 많은 것을 한칸 뒤로 이동시켜준다.
            elif nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, cnt+1))

print(-1)
