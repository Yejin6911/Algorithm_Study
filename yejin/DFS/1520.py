import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    # 방문하지 않은 경우
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]  # 해당 위치까지 가는 내리막길 경로의 수를 저장
print(dfs(0, 0))
