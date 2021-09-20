import sys
input = sys.stdin.readline

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북:0, 동:1, 남:2, 서:3
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    # 왼쪽 회전
    check = False
    for i in range(4):
        nd = ((d-1)+4) % 4
        nr = r + dir[nd][0]
        nc = c + dir[nd][1]
        if board[nr][nc] == 0:
            check = True
            r = nr
            c = nc
            d = nd
            break
        else:
            d = nd
    # 네방향 모두 청소 되어있거나 벽인 경우
    if not check:
        nr = r - dir[d][0]
        nc = c - dir[d][1]
        if board[nr][nc] == 1:
            break
        else:
            r = nr
            c = nc

print(cnt)
