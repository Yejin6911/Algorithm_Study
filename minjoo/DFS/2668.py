import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = [[] for _ in range(n+1)]
for i in range(1, n+1):
    nums[int(input())].append(i)

def dfs(u, visited):
    visited.append(u) # 방문한 노드 담아줌
    checked[u] = 1
    for v in nums[u]:
        if(v not in visited):
            dfs(v, visited.copy())
        else: # 사이클이 생기면 뽑는다
            result.extend(visited)
            return


checked = [0 for _ in range(n+1)] # 탐색 여부 확인
result = []

for i in range(1, n+1):
    if(checked[i] == 0):
        dfs(i, [])

result.sort()
print(len(result))
for x in result:
    print(x)