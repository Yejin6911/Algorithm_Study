dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

r, c = map(int, input().split()) # 세로, 가로
board = [list(input()) for _ in range(r)]
answer = 1

def bfs(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0<=nx<r and 0<=ny<c and board[nx][ny] not in ans):
                q.add((nx, ny, ans+board[nx][ny]))
                answer = max(answer, len(ans)+1)

bfs(0, 0)
print(answer)