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
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and not visited[nx][ny]:
                global area
                area += 1
                dfs(nx, ny)


# 직사각형 색칠
def paint(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1


m, n, k = map(int, input().rstrip().split())
matrix = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().rstrip().strip().split())
    paint(x1, y1, x2, y2)
for i in range(n):
    for j in range(m):
        area = 1
        if matrix[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            result.append(area)

print(len(result))
for area in sorted(result):
    print(area, end=' ')
