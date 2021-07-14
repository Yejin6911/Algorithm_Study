import sys
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = 1
    for e in board[v]:
        if(visited[e] == 0):
            dfs(e)

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

for i in range(1, n+1):
    if(visited[i] == 0):
        dfs(i)
        count += 1

print(count)
