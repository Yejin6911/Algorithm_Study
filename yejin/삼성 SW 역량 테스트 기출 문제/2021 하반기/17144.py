import sys
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def spread(board):
    new_board = copy.deepcopy(board)
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                mount = board[x][y]//5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        new_board[nx][ny] += mount
                        new_board[x][y] -= mount
    return new_board


def clean(board):
    new_board = copy.deepcopy(board)
    # 윗부분
    d = 3
    x, y = air[0][0], air[0][1]+1
    new_board[x][y] = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if (nx, ny) == air[0]:
            break
        if not (0 <= nx < r and 0 <= ny < c):
            d = (d+1) % 4
            continue
        else:
            new_board[nx][ny] = board[x][y]
            x, y = nx, ny
    # 아랫부분
    d = 3
    x, y = air[1][0], air[1][1]+1
    new_board[x][y] = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if (nx, ny) == air[1]:
            break
        if not (0 <= nx < r and 0 <= ny < c):
            d = (d-1) % 4
            continue
        else:
            new_board[nx][ny] = board[x][y]
            x, y = nx, ny
    return new_board


r, c, t = map(int, input().split())
board = []
air = []
for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] == -1:
            air.append((i, j))
    board.append(row)

for _ in range(t):
    board = spread(board)
    board = clean(board)

total = 0
for row in board:
    total += sum(row)
print(total+2)  # 공기청청기 -1 제외해주고 출력
