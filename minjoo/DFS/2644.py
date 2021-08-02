from collections import deque


n = int(input())
q1, q2 = map(int, input().split())

m = int(input())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(v, target):
    count = 0
    q = deque([[v, count]])
    while(q):
        value = q.popleft()
        v = value[0]
        count = value[1]
        if(v == target):
            return count
        if(not visited[v]):
            count += 1
            visited[v] = True
            for e in adj[v]:
                if(not visited[e]):
                    q.append([e, count])
    return -1

print(bfs(q1, q2))