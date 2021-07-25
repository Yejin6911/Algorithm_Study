import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, group):
    visited[start] = group
    for i in graph[start]:
        if visited[i] == 0:
            # 방문하지 않은 경우 다른 그룹으로 설정하여 dfs실행
            if not dfs(i, -group):
                # 인접한 노드가 같은 그룹인 경우 False 리턴
                return False
        # 이미 방문한 인접노드와 현재 노드가 같은 그룹인 경우
        elif visited[i] == visited[start]:
            return False
    return True


k = int(input().rstrip())
for _ in range(k):
    v, e = map(int, input().rstrip().split())
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for i in range(e):
        v1, v2 = map(int, input().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    result = True
    for i in range(1, v+1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    print("YES" if result else "NO")
