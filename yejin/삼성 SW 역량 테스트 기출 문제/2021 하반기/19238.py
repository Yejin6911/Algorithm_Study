from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def findDist():
    distances = [0]
    for i in range(1, m+1):
        visited = [[0]*n for _ in range(n)]
        start = starts[i]
        end = ends[i]
        queue = deque()
        queue.append((start, 0))
        visited[start[0]][start[1]] = 1
        check = False
        while queue:
            now = queue.popleft()
            if now[0] == end:
                distances.append(now[1])
                check = True
                break
            for i in range(4):
                nx = now[0][0]+dx[i]
                ny = now[0][1]+dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append(((nx, ny), now[1]+1))
        if not check:
            distances.append(-1)
    return distances


def search(x, y):
    candidates = []
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = 1
    while queue:
        now = queue.popleft()
        if board[now[0]][now[1]] > 0:
            candidates.append(now)
        else:
            for i in range(4):
                nx = now[0]+dx[i]
                ny = now[1]+dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, now[2]+1))
    return candidates


n, m, fuel = map(int, input().rstrip().split())
board = []
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(n):
        if row[j] == 1:
            row[j] = -1  # 벽: -1
    board.append(row)

x, y = map(int, input().rstrip().split())
x -= 1
y -= 1

starts = [0]
ends = [0]
for i in range(1, m+1):
    a, b, c, d = map(int, input().rstrip().split())
    starts.append((a-1, b-1))
    board[a-1][b-1] = i
    ends.append((c-1, d-1))
distances = findDist()

# 출발지점에서 도착지점으로 못가는 경우가 있는 경우
if -1 in distances:
    print(-1)
else:
    for _ in range(m):
        candidates = search(x, y)  # [(x,y,dist)]
        if not len(candidates):
            fuel = -1
            break
        candidates.sort(key=lambda x: (x[2], x[0], x[1]))
        customer = candidates[0]
        idx = starts.index((customer[0], customer[1]))
        start = starts[idx]
        end = ends[idx]
        dist = distances[idx]
        if customer[2] + dist > fuel:
            fuel = -1
            break
        board[start[0]][start[1]] = 0
        x = end[0]
        y = end[1]
        fuel = fuel-customer[2]+dist
    print(fuel)
