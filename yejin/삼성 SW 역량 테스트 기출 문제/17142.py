import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline


# bfs
def spread():
    while queue:
        global cnt
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
                visited[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny))
                now_board[nx][ny] = now_board[x][y] + 1


n, m = map(int, input().rstrip().split())
board = []
virus = []
total = n*n
max_time = sys.maxsize
result = max_time
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(n):
        # 바이러스인 경우
        if row[j] == 2:
            virus.append((i, j))
        # 벽인 경우
        elif row[j] == 1:
            total -= 1
    board.append(row)


select = list(combinations(virus, m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(len(select)):
    # 방문 여부 저장
    visited = [[0]*n for _ in range(n)]
    # 퍼진 시간 저장
    now_board = [[-1]*n for _ in range(n)]
    active = select[i]
    queue = deque()
    for v in active:
        visited[v[0]][v[1]] = 1
        now_board[v[0]][v[1]] = 0
        queue.append((v[0], v[1]))
    cnt = m
    spread()
    if total-cnt == 0:
        time = 0
        for x in range(n):
            for y in range(n):
                # 비활성화 바이러스는 고려 x
                if board[x][y] != 1 and (x, y) not in virus:
                    time = max(time, now_board[x][y])
        result = min(result, time)

if result == max_time:
    print(-1)
else:
    print(result)
