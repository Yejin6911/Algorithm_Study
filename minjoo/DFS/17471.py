from collections import defaultdict, deque
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
g = defaultdict(list)

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]+1):
        g[i].append(temp[j]-1)

def bfs(combi):
    start = combi[0]
    q = deque([start])
    visited = set([start])
    sum = 0
    while(q):
        v = q.popleft()
        sum += p[v]
        for u in g[v]:
            if u not in visited and u in combi:
                q.append(u)
                visited.add(u)
    return sum, len(visited)

result = sys.maxsize

for i in range(1, n//2+1):
    combis = list(combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if(v1 + v2 == n): # 2번의 bfs를 통해 모든 노드가 방문되었는지 확인
            result = min(result, abs(sum1 - sum2))


if(result != sys.maxsize):
    print(result)
else:
    print(-1)
                


