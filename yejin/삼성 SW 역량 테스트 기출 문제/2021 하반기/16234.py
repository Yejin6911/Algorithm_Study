from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# dfs 시간초과
# def dfs(x, y):
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if l <= abs(matrix[x][y] - matrix[nx][ny]) <= r and not checked[nx][ny]:
#                 checked[nx][ny] = 1
#                 group.append((nx, ny))
#                 dfs(nx, ny)


def move(group):
    sum = 0
    for i in group:
        sum += matrix[i[0]][i[1]]
    new_num = sum//len(group)
    for i in group:
        matrix[i[0]][i[1]] = new_num


def bfs(x, y):
    group = [(x, y)]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(matrix[x][y] - matrix[nx][ny]) <= r and not checked[nx][ny]:
                checked[nx][ny] = 1
                queue.append((nx, ny))
                group.append((nx, ny))
    return group


cnt = 0
while True:
    checked = [[0]*n for _ in range(n)]
    check = False
    for x in range(n):
        for y in range(n):
            if not checked[x][y]:
                checked[x][y] = 1
                group = bfs(x, y)
                # group = [(x, y)]
                # dfs(x, y)
                if len(group) > 1:
                    check = True
                    move(group)
    # 연합 할 수 없는 경우
    if not check:
        break
    else:
        cnt += 1

print(cnt)
