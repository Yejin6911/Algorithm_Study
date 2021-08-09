import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start):
    visited[start] = 1
    if tree[start]:
        for node in tree[start]:
            dfs(node)


def find_leaf(start):
    if not len(new_tree[start]):
        global cnt
        cnt += 1
        return
    else:
        for node in new_tree[start]:
            find_leaf(node)


n = int(input())
tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))
for i in range(n):
    if parents[i] != -1:
        tree[parents[i]].append(i)

# 삭제 할 노드
delete = int(input())

# 삭제 노드가 루트노드인 경우
if parents[delete] == -1:
    print(0)
    sys.exit()

# 노드 삭제
visited = [0 for _ in range(n)]
dfs(delete)
new_tree = copy.deepcopy(tree)
new_tree[parents[delete]].remove(delete)

# 삭제 노드의 자식 노드 삭제
for i in range(n):
    if visited[i] == 1:
        new_tree[i] = []

cnt = 0
root = parents.index(-1)
# 리프 노드 개수  탐색
find_leaf(root)
print(cnt)
