dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
board = [list(input()) for _ in range(n)]
pos = [[0 for _ in range(n)] for _ in range(n)] # 적록색약인 사람
neg = [[0 for _ in range(n)] for _ in range(n)] # 정상인 사람

for i in range(n):
    for j in range(n):
        if(board[i][j] == 'R'):
            pass
        elif(board[i][j] == 'G'):
            neg[i][j] = 2
        else:
            pos[i][j] = 1
            neg[i][j] = 1

def dfs(x, y, board, num):
    global visited
    q = set([(x, y)])
    while(q):
        x, y = q.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and board[nx][ny] == num):
                q.add((nx, ny))

a1, a2 = 0, 0

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(visited[i][j] == 0):
            dfs(i, j, pos, pos[i][j])
            a1 += 1
            
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(visited[i][j] == 0):
            dfs(i, j, neg, neg[i][j])
            a2 += 1
        
print(a2, a1)