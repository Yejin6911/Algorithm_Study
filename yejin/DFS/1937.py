# PyPy3으로 돌리면 메모리초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 깊이우선탐색해서 해당 칸에서 최대 이동 가능한 칸의 수 return
def dfs(x, y):
    # 이미 방문 한 경우
    if visited[x][y]:
        return visited[x][y]
    # 아직 방문 안한 경우
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
            # 이동할 수 있는 칸의 수 update
            visited[x][y] = max(visited[x][y], dfs(nx, ny)+1)
    return visited[x][y]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = 0
for x in range(n):
    for y in range(n):
        result = max(result, dfs(x, y))

print(result)
