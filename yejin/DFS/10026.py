import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[x][y] == matrix[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]


result1 = 0
visited = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result1 += 1
            dfs(i, j)

# 색맹인 사람
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

result2 = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result2 += 1
            dfs(i, j)

print(result1, result2)
