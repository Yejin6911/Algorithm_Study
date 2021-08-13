import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 세로, 가로, 음식물쓰레기 개수
board = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
def bfs(x, y):
    cnt = 0
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while(q):
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(1<=nx<n+1 and 1<=ny<m+1):
                if(visited[nx][ny] == 0 and board[nx][ny] == 1):
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return cnt

answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if(board[i][j] == 1 and visited[i][j] == 0):
            answer = max(answer, bfs(i, j))

print(answer)