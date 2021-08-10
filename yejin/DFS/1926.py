import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and not visited[nx][ny]:
            global cnt
            cnt += 1
            dfs(nx, ny)


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            result.append(cnt)

# 그림이 없는 경우
if not len(result):
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))
