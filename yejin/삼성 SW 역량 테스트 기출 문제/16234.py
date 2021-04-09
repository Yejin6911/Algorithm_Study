import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# python3 는 시간초과 pypy3으로 제출


# 인구 이동
def move(group):
    total = 0
    for i in group:
        total += A[i[0]][i[1]]
    num = int(total/len(group))
    for i in group:
        A[i[0]][i[1]] = num


# 연합그룹 생성
def bfs(x, y):
    group = [(x, y)]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(A[x][y] - A[nx][ny]) <= r and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                group.append((nx, ny))
    return group


cnt = 0
while True:
    visited = [[0]*n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                new_group = bfs(i, j)
                if len(new_group) > 1:
                    check = True
                    move(new_group)
    if not check:
        break
    cnt += 1

print(cnt)
