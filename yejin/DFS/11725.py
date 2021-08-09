import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    for v in tree[node]:
        if parents[v] == 0 and v != 1:
            parents[v] = node
            dfs(v)


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(n+1)]

dfs(1)
for p in parents[2:]:
    print(p)
