import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# PyPy3은 메모리 에러, Python3로 통과

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    M[x][y] = -1  # 외부 공기 -1로 변경
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 외부 공기인 경우
            if M[nx][ny] == 0:
                dfs(nx, ny)


n, m = map(int, input().split())
M = []
cheese = deque()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            cheese.append((i, j))
    M.append(row)

# 치즈는 가장자리에 존재하지 않는다.
# -> 어느 가장자리 지점에서 bfs 혹은 dfs를 통해 치즈가 아닌 경우 -1로 변경
# -> 외부공기와 내부 공기를 분리할 수 있다.
dfs(0, 0)

result = 0
while cheese:
    result += 1
    length = len(cheese)
    melt = []
    for _ in range(length):
        x, y = cheese.popleft()
        cnt = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if M[nx][ny] == -1:
                cnt += 1
        # 2면 이상 닿은 경우
        if cnt >= 2:
            M[x][y] = 0
            melt.append((x, y))
        # 2면 미만으로 닿은 경우
        else:
            cheese.append((x, y))

    # 녹는 지점을 기준으로 내부공기 였던 부분 외부공기와 연결 된 경우 수정
    # 녹는 지점도 외부공기로 처리
    for x, y in melt:
        dfs(x, y)

print(result)
