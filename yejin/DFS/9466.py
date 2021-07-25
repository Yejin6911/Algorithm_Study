import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    visited[x] = 1
    team.append(x)

    # 더이상 방문할 곳 없는 경우
    if visited[choice[x]]:
        if choice[x] in team:
            global cnt
            # 시작점과 끝점이 같아야 하므로 choice[x]부터 끝까지가 한 팀
            cnt += len(team[team.index(choice[x]):])
            return
    else:
        dfs(choice[x])


t = int(input())
for _ in range(t):
    n = int(input())
    choice = [0]+list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(n-cnt)
