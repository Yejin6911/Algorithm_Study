import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
now = (r, c)
board = [list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(n)]

# 0:북/1:동/2:남/3:서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]


def search(d, x, y):
    check = False
    for _ in range(4):
        d = (d-1+4) % 4
        nx = x+dx[d]
        ny = y+dy[d]
        if board[nx][ny] == 0:
            check = True
            x = nx
            y = ny
            break
    return check, x, y, d


# 처음 위치 처리
cnt = 0
x = now[0]
y = now[1]
check = True

while True:
    # 1. 현재 위치 청소
    if check:
        board[x][y] = 2
        cnt += 1
    # 왼쪽으로 돌면서 확인
    check, nx, ny, d = search(d, x, y)
    # 이동 가능한 경우
    if check:
        x = nx
        y = ny
    # 이동 불가능한 경우 - 후진
    else:
        x -= dx[d]
        y -= dy[d]
        if board[x][y] == 1:
            break


print(cnt)
