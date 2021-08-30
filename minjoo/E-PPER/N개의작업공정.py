n, r = map(int, input().split()) # 공정 수, 관계 수
time = list(map(int, input().split())) # 각 공정에서 소요되는 시간

rel = [[] for _ in range(n)]
for _ in range(r):
    x, y = map(int, input().split())
    rel[x-1].append(y-1)

goal = int(input())
goal -= 1

ans = 0
def dfs(i, t):
    global ans
    if(i == goal): # 목표 공정에 도달하면
        ans = max(ans, t)
        return

    for j in range(len(rel[i])): # 연결된 다음 공정에 대해
        nt = t + time[rel[i][j]] # 공정에 걸리는 시간 +
        dfs(rel[i][j], nt)

for i in range(n):
    dfs(i, time[i])
print(ans)