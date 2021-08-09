# 트리의 지름 구하기: 노드 x에서 가장 먼 노드를 y라고 했을 때
# y는 지름을 이루는 노드 중 하나이다.
# --> 임의의 노드 x에 대해서 dfs(x)에서 최장거리를 이루는 y를 구하고
# dfs(y)를 통해 최장 길이를 구하면 노드의 지름을 구할 수 있음.

import sys
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, length = map(int, input().split())
    tree[x].append([y, length])
    tree[y].append([x, length])

# print(tree)

result1 = [0 for _ in range(n+1)]

def dfs(start, tree, result):
    for y, length in tree[start]:
        if(result[y] == 0):
            result[y] = result[start] + length
            dfs(y, tree, result)

dfs(1, tree, result1)
result1[1] = 0

tmpmax = 0
index = 0

for i in range(len(result1)):
    if(tmpmax < result1[i]):
        tmpmax = result1[i]
        index = i

result2 = [0 for _ in range(n+1)]
dfs(index, tree, result2)
result2[index] = 0
print(max(result2))