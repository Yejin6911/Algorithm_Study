import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    area = 0
    while(q):
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m):
                if(board[nx][ny] == 1 and visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return area

cnt = 0
maxarea = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(board[i][j] == 1 and visited[i][j] == 0):
            area = bfs(i, j)
            cnt += 1
            maxarea = max(maxarea, area)

print(cnt)
print(maxarea)

