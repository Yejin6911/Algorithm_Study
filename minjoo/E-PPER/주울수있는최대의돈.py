import sys
sys.setrecursionlimit(10**6)

n = int(input())
money = list(map(int, input().split()))

visited = [0 for _ in range(n)]

ans = 0
def dfs(idx, m, visited):
    global ans
    # 마지막 인덱스에 다다를 경우
    if(idx == n):
        ans = max(ans, m)
        return

    if(idx < 2):
        # 선택하거나
        nm = m + money[idx]
        visited[idx] = 1
        dfs(idx+1, nm, visited)
        # 안하거나
        visited[idx] = 0
        dfs(idx+1, m, visited)
        return

    # idx 3부터
    if(visited[idx-1] and visited[idx-2]):
        # 이전 두개가 방문되었으면 선택 안함
        dfs(idx+1, m, visited)
    else:
        # 선택하거나
        nm = m + money[idx]
        visited[idx] = 1
        dfs(idx+1, nm, visited)
        # 안하거나
        visited[idx] = 0
        dfs(idx+1, m, visited)
        return
    
dfs(0, 0, visited)
print(ans)