import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(start):
    visited[start] = 1
    for i in range(1, n+1):
        if matrix[start][i] == 1 and visited[i] == 0:
            dfs(i)


n, m = map(int, input().rstrip().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().rstrip().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
