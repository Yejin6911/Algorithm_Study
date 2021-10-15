# PyPy3 제출 Python3 시간초과..
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
virus = []
board = []
blank = 0
for i in range(n):
    row = list(map(int, input().split()))
    blank += row.count(0)
    for j in range(n):
        if row[j] == 2:
            virus.append((i, j))
    board.append(row)

# 전체 경우의 수
candidates = list(combinations(virus, m))
result = INF

for candidate in candidates:
    now_blank = blank
    visited = [[-1]*n for _ in range(n)]
    for x, y in candidate:
        visited[x][y] = 0
    queue = deque(candidate)
    total_time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx, ny))
                # 빈칸일 때만 시간 비교후 update(퍼지지 않은 비활성화 바이러스 시간은 고려 x)
                if board[nx][ny] == 0:
                    now_blank -= 1
                    total_time = max(total_time, visited[nx][ny])
    if now_blank == 0:
        result = min(result, total_time)


if result == INF:
    print(-1)
else:
    print(result)
