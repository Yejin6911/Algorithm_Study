import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, weight):
    for node, w in tree[start]:
        if weight[node] == 0:
            weight[node] = weight[start]+w
            dfs(node, weight)


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

# 루트브터 해당 노드까지의 거리
weight_1 = [0 for _ in range(n+1)]
# 루트부터 각각의 노드까지의 거리찾기
dfs(1, weight_1)
# 시작점 거리 0으로 설정
weight_1[1] = 0

weight_2 = [0 for _ in range(n+1)]
start = weight_1.index(max(weight_1))
# 가장 먼 노드에서 DFS다시 실행
dfs(start, weight_2)
# 시작점 거리 0으로 설정
weight_2[start] = 0

# 거리 최대값 출력
print(max(weight_2))
