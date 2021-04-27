import sys
import copy
input = sys.stdin.readline

n = int(input().rstrip())
A = [list(map(int, input().rstrip().split())) for _ in range(n)]

x, y = n//2, n//2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d_1 = 0
d_2 = 1

D = [[(-1, 1), (1, 1), (-2, 0), (2, 0), (0, -2), (-1, 0), (1, 0), (-1, -1), (1, -1), (0, -1)],
     [(-1, -1), (-1, 1), (0, -2), (0, 2), (2, 0), (0, -1), (0, 1), (1, -1), (1, 1), (1, 0)],
     [(-1, -1), (1, -1), (-2, 0), (2, 0), (0, 2), (-1, 0), (1, 0), (-1, 1), (1, 1), (0, 1)],
     [(1, -1), (1, 1), (0, -2), (0, 2), (-2, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0)]]

ratio = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1]


def move(x, y, d):
    global result
    sand = A[x][y]
    dir = D[d]
    for i in range(len(dir)):
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        if i == len(dir)-1:
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                result += A[x][y]
            else:
                A[nx][ny] += A[x][y]
            A[x][y] = 0
        else:
            amount = int(sand*ratio[i])
            # 범위 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                result += amount
                A[x][y] -= amount
            else:
                A[x][y] -= amount
                A[nx][ny] += amount


result = 0
for i in range(1, n):
    #가로
    for _ in range(i):
        nx = x+dx[d_1]
        ny = y+dy[d_1]
        move(nx, ny, d_1)
        x, y = nx, ny
    d_1 = (d_1+2) % 4
    # 세로
    for _ in range(i):
        nx = x+dx[d_2]
        ny = y+dy[d_2]
        move(nx, ny, d_2)
        x, y = nx, ny
    d_2 = (d_2+2) % 4
    if i == n-1:
        for _ in range(i):
            nx = x+dx[d_1]
            ny = y+dy[d_1]
            move(nx, ny, d_1)
            x, y = nx, ny
print(result)
