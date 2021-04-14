
import sys
input = sys.stdin.readline


def move():
    new = [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if len(board[x][y]):
                s, d, z = board[x][y].pop()
                nx, ny = x, y
                for _ in range(s):
                    nx += dx[d-1]
                    ny += dy[d-1]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        if d % 2:
                            d += 1
                        else:
                            d -= 1
                        nx += dx[d-1]*2
                        ny += dy[d-1]*2
                if len(new[nx][ny]):
                    if new[nx][ny][0][2] < z:
                        new[nx][ny] = [(s, d, z)]
                else:
                    new[nx][ny].append((s, d, z))
    return new


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

r, c, m = map(int, input().rstrip().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for i in range(m):
    x, y, s, d, z = map(int, input().rstrip().split())
    board[x-1][y-1].append((s, d, z))

result = 0
for i in range(c):
    # 1. 해당 열에 상어 있으면 잡는다.
    for j in range(r):
        if len(board[j][i]):
            result += board[j][i].pop()[2]
            break
    # 2. 상어 이동
    board = move()

print(result)
