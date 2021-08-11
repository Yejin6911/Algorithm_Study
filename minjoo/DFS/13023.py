import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relation = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [0]*n

def dfs(x, number):
    if(number == 4):
        print(1)
        exit()
    for i in relation[x]:
        if(not visited[i]):
            visited[i] = 1
            dfs(i, number+1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0)
