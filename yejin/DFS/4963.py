import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def bfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if matrix[nx][ny] == 1 and not visited[nx][ny]:
                bfs(nx, ny)


result = []
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().rstrip().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    result.append(cnt)


for cnt in result:
    print(cnt)
