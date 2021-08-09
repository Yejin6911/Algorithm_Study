import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 방법 기억하기!!
def dfs(start, weight):
    for n, w in tree[start]:
        if weight[n] == 0:
            weight[n] = weight[start]+w
            dfs(n, weight)


v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        tree[node].append((data[i], data[i+1]))

# 첫번째 DFS
weight1 = [0 for _ in range(v+1)]
dfs(1, weight1)
weight1[1] = 0

# 가장 먼 노드로 DFS 한번 더
new_start = weight1.index(max(weight1))
weight2 = [0 for _ in range(v+1)]
dfs(new_start, weight2)
weight2[new_start] = 0

print(max(weight2))
