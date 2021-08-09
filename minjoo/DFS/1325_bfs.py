import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
relation = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0 for _ in range(n+1)]
    visited[x] = 1
    cnt = 0
    while(q):
        x = q.popleft()
        for i in relation[x]:
            if(visited[i] == 0):
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

ans = []
maxans = 0
for i in range(1, n+1):
    cnt = bfs(i)
    if(maxans < cnt):
        maxans = cnt
        ans = [i]
    elif(maxans == cnt):
        ans.append(i)

print(*ans)

