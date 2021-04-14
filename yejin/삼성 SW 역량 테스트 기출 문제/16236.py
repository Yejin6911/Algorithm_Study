import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
board = []
shark = (0, 0)
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    board.append(row)
    for j in range(n):
        if row[j] == 9:
            shark = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 먹을 수 있는 물고기 탐색
def find(x, y, size):
    fish = []
    visited = [[0]*n for _ in range(n)]
    queue = deque([(x, y, 0)])
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 물고기 있는 경우
            if 1 <= board[nx][ny] <= 6 and not visited[nx][ny]:
                # 먹을 수 있는 경우
                if board[nx][ny] < size:
                    visited[nx][ny] = 1
                    fish.append((nx, ny, dist+1))
                # 크기가 같아 지나갈 수 있는 경우
                elif board[nx][ny] == size:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist+1))
            # 물고기 없는 경우
            elif board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist+1))
    return fish


cnt = 0
result = 0
x, y, size, cnt = shark[0], shark[1], 2, 0
while True:
    fish = find(x, y, size)
    if not len(fish):
        break
    fish.sort(key=lambda x: (x[2], x[0], x[1]))
    eat = fish[0]
    board[x][y] = 0
    board[eat[0]][eat[1]] = 9
    x = eat[0]
    y = eat[1]
    cnt += 1
    result += eat[2]
    if cnt == size:
        size += 1
        cnt = 0

print(result)
