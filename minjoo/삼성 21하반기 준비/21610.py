import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
dx2, dy2 = [-1, -1, 1, 1], [-1, 1, 1, -1]

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for idx in range(m):
    rain = []
    d, s = move[idx]

    for i in range(len(cloud)):
        x, y = cloud[i]
        nx = (x + (dx[d-1] * s)) % n
        ny = (y + (dy[d-1] * s)) % n

        rain.append((nx, ny))
        board[nx][ny] += 1

    for i in range(len(rain)):
        x, y = rain[i]
        cnt = 0
        for j in range(4):
            nx = x + dx2[j]
            ny = y + dy2[j]
            if(0<=nx<n and 0<=ny<n and board[nx][ny] > 0):
                cnt += 1
        board[x][y] += cnt
   
    newcloud = []
    for i in range(n):
        for j in range(n):
            if(board[i][j] >= 2 and (i, j) not in rain):
                newcloud.append((i, j))
                board[i][j] -= 2

    cloud = deepcopy(newcloud)


_sum = 0
for i in range(n):
    for j in range(n):
        _sum += board[i][j]

print(_sum)