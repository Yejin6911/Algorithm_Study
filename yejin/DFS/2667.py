
import sys

input = sys.stdin.readline

n = int(input().rstrip())
M = [list(map(int, input().rstrip())) for x in range(n)]

visited = [[0]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cnt):
    visited[x][y] = cnt
    global num
    if M[x][y] == 1:
        num += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and M[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny, cnt)


cnt = 1
result = []
num = 0
for i in range(n):
    for j in range(n):
        if M[i][j] == 1 and not visited[i][j]:
            dfs(i, j, cnt)
            result.append(num)
            num = 0  # 단지별 아파트 개수 초기화
            cnt += 1

print(len(result))
for i in sorted(result):
    print(i)
