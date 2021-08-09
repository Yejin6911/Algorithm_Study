import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# DFS 메모리 초과 또는 시간초과
# def dfs(start):
#     if not len(data[start]):
#         return
#     for i in data[start]:
#         visited[i] = visited[start]+1
#         dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    cnt = 1
    while q:
        now = q.popleft()
        for i in data[now]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[b].append(a)

result = []
max_num = 0
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    cnt = bfs(i)
    if cnt == max_num:
        result.append(i)
    if max_num < cnt:
        max_num = cnt
        result = [i]
print(*result)
