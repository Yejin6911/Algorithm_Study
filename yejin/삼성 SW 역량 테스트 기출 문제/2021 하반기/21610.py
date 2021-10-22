dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def move(d, s):
    new_cloud = []
    for x, y in cloud:
        nx = (x+dx[d]*s) % n
        ny = (y+dy[d]*s) % n
        # 비내림
        board[nx][ny] += 1
        new_cloud.append((nx, ny))
    return new_cloud


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
M = [list(map(int, input().split())) for _ in range(m)]

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for d, s in M:
    new_cloud = move(d-1, s)
    for x, y in new_cloud:
        cnt = 0
        # 대각선 방향 에 물이 있는 경우
        for i in (1, 3, 5, 7):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        # 물 증가
        board[x][y] += cnt
    cloud = []
    for x in range(n):
        for y in range(n):
            if board[x][y] >= 2 and (x, y) not in new_cloud:
                board[x][y] -= 2
                cloud.append((x, y))
total = 0
for r in board:
    total += sum(r)

print(total)
