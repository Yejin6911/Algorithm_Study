import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]

temp = list(map(int, input().split()))
for i in range(n):
    if(temp[i] == -1):
        continue
    tree[temp[i]].append(i)

d = int(input()) # 지울 노드

visited = [0 for _ in range(n)]
nums = []
def dfs(x):
    visited[x] = 1
    nums.append(x)
    for i in range(len(tree[x])):
        dfs(tree[x][i])
dfs(d)

cnt = 0
for i in range(n):
    flag = 0

    # 방문 안한 노드 중 자식노드 개수가 0이면 리프노드
    if(visited[i] == 0 and len(tree[i]) == 0):
        cnt += 1

    # 방문 안한 노드 중 지워진 노드들을 자식노드로 갖고있으면 리프노드
    elif(visited[i] == 0):
        for j in range(len(tree[i])):
            if(tree[i][j] in nums):
                pass
            else:
                flag = 1
                break
        if(not flag):
            cnt += 1

print(cnt)