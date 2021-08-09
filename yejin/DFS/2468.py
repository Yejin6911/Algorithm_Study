import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, limit):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] > limit and not visited[nx][ny]:
                dfs(nx, ny, limit)


result = 1  # 계속 틀린 이유,, 최소가 0이 아니라 1이라 초기값 1로 설정해야 함
for limit in range(max(map(max, matrix))):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > limit and not visited[i][j]:
                cnt += 1
                dfs(i, j, limit)
    result = max(result, cnt)

print(result)
