import sys

input = sys.stdin.readline

n = int(input().rstrip())
link = int(input().rstrip())
data = [[0]*n for _ in range(n)]
for _ in range(link):
    a, b = map(int, input().rstrip().split())
    data[a-1][b-1], data[b-1][a-1] = 1, 1

visited = [0 for _ in range(n)]


# dfs
def dfs(start):
    visited[start] = 1
    global cnt
    for i in range(n):
        if i != start and data[start][i] == 1 and not visited[i]:
            cnt += 1
            dfs(i)


cnt = 0
dfs(0)
print(cnt)
