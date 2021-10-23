import sys
input = sys.stdin.readline


def SpringToSummer():
    for x in range(n):
        for y in range(n):
            if len(board[x][y]):
                board[x][y].sort()
                for t in range(len(board[x][y])):
                    # 나무 나이 증가(봄)
                    if B[x][y] >= board[x][y][t]:
                        B[x][y] -= board[x][y][t]
                        board[x][y][t] += 1
                    # 죽은 나무 양분처리(여름)
                    else:
                        for i in range(t, len(board[x][y])):
                            B[x][y] += board[x][y][i]//2
                        board[x][y] = board[x][y][:t]
                        break


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def FallToWinter():
    for x in range(n):
        for y in range(n):
            if len(board[x][y]):
                for tree in board[x][y]:
                    if tree % 5 == 0:
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                board[nx][ny].append(1)
            # 양분 증가
            B[x][y] += A[x][y]


n, m, k = map(int, input().split())
B = [[5]*n for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]

board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    board[x-1][y-1].append(z)

for _ in range(k):
    SpringToSummer()
    FallToWinter()

cnt = 0
for x in range(n):
    for y in range(n):
        if len(board[x][y]):
            cnt += len(board[x][y])
print(cnt)
