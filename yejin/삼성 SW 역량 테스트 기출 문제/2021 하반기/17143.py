import sys
input = sys.stdin.readline


def catch(c):
    for i in range(R):
        if board[i][c]:
            catch = board[i][c][2]
            board[i][c] = []
            return catch
    return 0


dir = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]


def move():
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                s, d, z = board[x][y]
                nx, ny = x, y
                for i in range(s):
                    nx += dir[d][0]
                    ny += dir[d][1]
                    if not (0 <= nx < R and 0 <= ny < C):
                        if d == 1 or d == 3:
                            d += 1
                        else:
                            d -= 1
                        nx += (dir[d][0]*2)
                        ny += (dir[d][1]*2)
                # 이미 상어 존재하는 경우
                if new_board[nx][ny]:
                    # 잡아먹는 경우
                    if new_board[nx][ny][2] < z:
                        new_board[nx][ny] = [s, d, z]
                else:
                    new_board[nx][ny] = [s, d, z]
    return new_board


R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = [s, d, z]

total = 0
for i in range(C):
    total += catch(i)
    board = move()

print(total)
