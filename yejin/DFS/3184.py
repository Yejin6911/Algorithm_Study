import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs_1(x, y):
    checked[x][y] = 1
    if matrix[x][y] == 'v':
        global wolf
        wolf += 1
    elif matrix[x][y] == 'o':
        global sheep
        sheep += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 < nx < r-1 and 0 < ny < c-1:
            if matrix[nx][ny] != '#' and not checked[nx][ny]:
                dfs_1(nx, ny)


r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
checked = [[0]*c for _ in range(r)]

total_wolf = 0
total_sheep = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if matrix[i][j] != '#' and not checked[i][j]:
            # 새로운 영역
            sheep = 0
            wolf = 0
            dfs_1(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)
