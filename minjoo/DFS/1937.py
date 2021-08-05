# dp 문제!!!!!
# https://hooongs.tistory.com/178
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if(dp[x][y] == 1):
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<n and board[nx][ny]>board[x][y]):
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
            # 상하좌우 중 더 큰 곳만 살피는데, 
            # 거기에 값이 있다면 본인 좌표에는 그 값 + 1을 넣으면 됨
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
        

print(ans)