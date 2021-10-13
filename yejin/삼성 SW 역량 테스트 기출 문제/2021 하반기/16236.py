from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = []
shark = (0, 0)
size = 2
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 9:
            shark = (i, j)
    board.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 먹을 수 있는 물고기 찾기


def canEat():
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([shark[0], shark[1], 0])
    visited[shark[0]][shark[1]] = 1
    candidates = []
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                if board[nx][ny] == 0 or board[nx][ny] == size:
                    q.append([nx, ny, dist+1])
                elif 0 < board[nx][ny] < size:
                    candidates.append([nx, ny, dist+1])
    # 거리, 위치 순으로 정렬
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    return candidates


time = 0
cnt = 0
while True:
    fish = canEat()
    if len(fish):
        # 가장 가까운 물고기
        nx, ny, dist = fish[0]
        time += dist
        board[shark[0]][shark[1]] = 0
        board[nx][ny] = 9
        shark = (nx, ny)
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    else:
        break
print(time)
