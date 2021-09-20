import sys
input = sys.stdin.readline


# 주사위 회전
def spin(d):
    if d == 1:  # 동
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif d == 2:  # 서
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif d == 3:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    else:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]


def copy(x, y):
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0


dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
# 주사위
dice = [0, 0, 0, 0, 0, 0]  # 상,하,좌,우,앞,뒤


# 처음 위치부분 처리
copy(x, y)
for d in moves:
    if 0 <= x+dir[d][0] < n and 0 <= y+dir[d][1] < m:
        x += dir[d][0]
        y += dir[d][1]
        spin(d)
        copy(x, y)
        print(dice[0])
    else:
        continue
