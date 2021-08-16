import sys
# import copy
from collections import deque
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 빙하마다 녹는 시간대 저장 및 마지막 빙하 녹는 시간 반환
def melt_time_set(lake):
    visited = [[0]*c for _ in range(r)]
    queue = deque()

    # 처음 바다 또는 백조인 경우
    for i in range(r):
        for j in range(c):
            if lake[i][j] != 'X':
                queue.append((i, j))
                time[i][j] = 0
                visited[i][j] = 1
    # 녹는데 가장 오래걸리는 시간
    last_time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if lake[nx][ny] == 'X' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    time[nx][ny] = time[x][y]+1
                    visited[nx][ny] = 1
                    last_time = time[nx][ny]
    return last_time


def bfs(start, mid, end):
    queue = deque()
    queue.append(start)
    visited = [[0]*c for _ in range(r)]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = 1
                # 백조끼리 만날 수 있는 경우
                if nx == end[0] and ny == end[1]:
                    return True
                # 기준 시간인 mid 시간보다 작은 경우 녹아서 이동 가능한 것으로 간주
                if time[nx][ny] <= mid:
                    queue.append((nx, ny))
    return False


r, c = map(int, input().split())
lake = []
swan = []
for i in range(r):
    row = list(input().rstrip())
    lake.append(row)
    for j in range(c):
        if row[j] == 'L':
            swan.append((i, j))

time = [[0]*c for _ in range(r)]
min_time = 0
max_time = melt_time_set(lake)
answer = max_time

# 이분탐색으로 시간 찾기
while min_time <= max_time:
    mid = (min_time+max_time) // 2
    if bfs(swan[0], mid, swan[1]):
        answer = mid
        max_time = mid-1
    else:
        min_time = mid+1

print(answer)

# 시간초과 코드....😭
# def melt(lake):
#     new_lake = copy.deepcopy(lake)
#     for x in range(r):
#         for y in range(c):
#             if lake[x][y] == 'X':
#                 cnt = 0
#                 for i in range(4):
#                     nx = x+dx[i]
#                     ny = y+dy[i]
#                     if 0 <= nx < r and 0 <= ny < c:
#                         if lake[nx][ny] == '.':
#                             cnt += 1
#                 if cnt:
#                     new_lake[x][y] = '.'
#     return new_lake


# def check(x, y):
#     visited[x][y] = 1
#     if (x, y) == swan[1]:
#         return
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             if lake[nx][ny] != 'X' and not visited[nx][ny]:
#                 check(nx, ny)


# r, c = map(int, input().split())
# lake = []
# swan = []
# for i in range(r):
#     row = list(input().rstrip())
#     lake.append(row)
#     for j in range(c):
#         if row[j] == 'L':
#             swan.append((i, j))

# answer = 0
# while True:
#     answer += 1
#     lake = melt(lake)
#     visited = [[0]*c for _ in range(r)]
#     check(swan[0][0], swan[0][1])
#     if visited[swan[1][0]][swan[1][1]] == 1:
#         break
# print(answer)
