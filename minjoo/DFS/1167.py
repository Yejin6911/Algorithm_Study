# 트리의 지름 구하기: 노드 x에서 가장 먼 노드를 y라고 했을 때
# y는 지름을 이루는 노드 중 하나이다.
# --> 임의의 노드 x에 대해서 dfs(x)에서 최장거리를 이루는 y를 구하고
# dfs(y)를 통해 최장 길이를 구하면 노드의 지름을 구할 수 있음.

import sys
sys.setrecursionlimit(10**9)

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1, 2):
        tree[temp[0]].append([temp[i], temp[i+1]])
        tree[temp[i]].append([temp[0], temp[i+1]])

# 첫번째 dfs 결과
result1 = [0 for _ in range(v+1)]

def dfs(start, tree, result):
    for y, length in tree[start]:
        if(result[y] == 0):
            result[y] = result[start] + length
            dfs(y, tree, result)

dfs(1, tree, result1) # 아무노드에서 시작
result1[1] = 0 

tmpmax = 0 # 최대값 구하기
index = 0 # 최장경로 노드

for i in range(len(result1)):
    if(tmpmax < result1[i]):
        tmpmax = result1[i]
        index = i

# 최장경로 노드에서 다시 dfs를 통해 트리지름 구하기
result2 = [0 for _ in range(v+1)]
dfs(index, tree, result2)
result2[index] = 0
print(max(result2))