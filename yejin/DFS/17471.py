from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(now, group):
    if group == 1:
        visited[now] = 1
        for c in group1:
            if c in city[now] and not visited[c]:
                dfs(c, 1)
    else:
        visited[now] = 2
        for c in group2:
            if c in city[now] and not visited[c]:
                dfs(c, 2)


def total(group):
    total = 0
    for i in group:
        total += population[i]
    return total


n = int(input())
population = list(map(int, input().split()))

city = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        city[i].append(data[j]-1)

inf = sys.maxsize
answer = inf
# 모든 경우의 수
for i in range(1, int(n//2)+1):
    picked = list(combinations([x for x in range(n)], i))
    for group in picked:
        group1 = list(group)
        group2 = [x for x in range(n) if x not in group1]
        visited = [0 for _ in range(n)]
        # 그룹 별로 깊이 우선 탐색
        dfs(group1[0], 1)
        dfs(group2[0], 2)
        # 2개의 그룹이 각각 모두 이어져 있는 경우
        if visited.count(1) == len(group1) and visited.count(2) == len(group2):
            answer = min(answer, abs(total(group1)-total(group2)))

if answer == inf:
    print(-1)
else:
    print(answer)
