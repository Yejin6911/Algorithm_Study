import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


n, m, k = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

visited = [[0]*m for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            result = max(result, cnt)
print(result)
