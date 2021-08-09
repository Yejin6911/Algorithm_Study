import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


T = int(input().rstrip())

for _ in range(T):
    m, n, k = map(int, input().rstrip().split())
    matrix = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        matrix[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)
