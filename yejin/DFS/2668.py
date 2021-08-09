import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 참고: https://cotak.tistory.com/141
# 참고: https://home-body.tistory.com/134


def dfs(now, first):
    visited[now] = 1
    for v in data[now]:
        if not visited[v]:
            dfs(v, first)
        else:
            # 사이클 생긴 경우
            if v == first:
                result.append(v)


n = int(input())
data = [[] for _ in range(n+1)]
for i in range(1, n+1):
    v = int(input())
    data[v].append(i)

result = []
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i, i)

print(len(result))
for i in result:
    print(i)
