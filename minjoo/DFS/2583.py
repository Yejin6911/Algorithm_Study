m, n, k = map(int, input().split()) # 세로, 가로, 직사각형 개수

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

board = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            board[i][j] = 1

visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    global visited
    q = set([(x, y)])
    cnt = 0
    while(q):
        x, y = q.pop()
        cnt += 1
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny] == 0):
                q.add((nx, ny))
                
    return cnt

ans = []
for i in range(n):
    for j in range(m):
        if(board[i][j] == 0 and visited[i][j] == 0):
            ans.append(bfs(i, j))

ans = sorted(ans)
print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=' ')
       
