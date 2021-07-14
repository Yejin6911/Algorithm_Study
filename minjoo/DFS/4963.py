import sys
sys.setrecursionlimit(10000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    global board, visited, m, n
    visited[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<m):
            if(board[nx][ny] == 1 and visited[nx][ny] == 0):
                dfs(nx, ny)


while(1):
    m, n = map(int, input().split()) # 지도의 너비, 높이
    ans = 0

    if(m == 0 and n == 0):
        break

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1 and visited[i][j] == 0):
                dfs(i, j)
                ans += 1
    print(ans)

