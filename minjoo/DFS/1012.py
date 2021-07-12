import sys

sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())

def dfs(x, y):
    global board, visited, n, m
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<m):
            if(board[nx][ny] == 1 and visited[nx][ny] == 0):
                dfs(nx, ny)

for _ in range(t):
    ans = 0

    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    board = [[0 for _ in range(m)] for _ in range(n)] # 배추밭
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1 and visited[i][j] == 0):
                dfs(i, j)
                ans += 1

    print(ans)