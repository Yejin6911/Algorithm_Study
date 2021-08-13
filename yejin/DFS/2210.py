import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num+matrix[nx][ny])


matrix = [input().split() for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
print(len(result))
