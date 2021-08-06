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