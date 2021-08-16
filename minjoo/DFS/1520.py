# dfs 시간초과 -> dfs + dp
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dp = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(x, y):

    if(x == (n-1) and y == (m-1)):
        return 1

    # 이미 방문한 정점이면 dp 값 리턴
    if(dp[x][y] != -1):
        return dp[x][y]

    # 처음 방문한 정점이라면 0으로 초기화
    dp[x][y] = 0

    # dfs 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<m):
            if(board[nx][ny] < board[x][y]):
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]  

print(dfs(0, 0))
