import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
relation = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    cnt = 0
    while(q):
        x = q.popleft()
        if(relation[x]):
            cnt += 1
            for nx in relation[x]:
                q.append(nx)
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

for i in ans:
    print(i, end=' ')

