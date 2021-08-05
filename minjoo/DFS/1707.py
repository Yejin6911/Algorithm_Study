from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

def bfs(start):
    group[start] = 1
    q = deque()
    q.append(start)
    while(q):
        a = q.popleft()
        for i in tree[a]:
            if(group[i] == 0):
                group[i] = -group[a]
                q.append(i)
            else:
                if(group[i] == group[a]):
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    flag = True
    tree = [[] for _ in range(v+1)]
    group = [0 for i in range(v+1)]

    for j in range(e):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    for j in range(1, v+1):
        if(group[j] == 0):
            if(not bfs(j)):
                flag = False
                break
    print("YES" if flag else "NO")