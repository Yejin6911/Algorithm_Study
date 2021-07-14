import sys
sys.setrecursionlimit(100000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())

board = []
min_h, max_h = sys.maxsize, 0
for _ in range(n):
    temp = list(map(int, input().split()))
    if(min(temp) < min_h):
        min_h = min(temp)
    if(max(temp) > max_h):
        max_h = max(temp)
    board.append(temp)

def dfs(x, y, h):
    global board, visited, n
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<n):
            if(board[nx][ny] > h and visited[nx][ny] == 0):
                dfs(nx, ny, h)

ans = 0

for h in range(min_h-1, max_h+1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if(board[i][j] > h and visited[i][j] == 0):
                dfs(i, j, h)
                cnt += 1
    
    if(ans < cnt):
        ans = cnt

print(ans)




