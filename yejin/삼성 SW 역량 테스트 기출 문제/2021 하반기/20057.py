dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

directions = [  # 1,2,7,10,5,a순
    [(-1, 1), (1, 1), (-2, 0), (2, 0), (-1, 0),
     (1, 0), (-1, -1), (1, -1), (0, -2), (0, -1)],
    [(-1, -1), (-1, 1), (0, -2), (0, 2), (0, -1),
     (0, 1), (1, -1), (1, 1), (2, 0), (1, 0)],
    [(-1, -1), (1, -1), (-2, 0), (2, 0), (-1, 0),
     (1, 0), (-1, 1), (1, 1), (0, 2), (0, 1)],
    [(1, -1), (1, 1), (0, -2), (0, 2), (0, -1),
     (0, 1), (-1, -1), (-1, 1), (-2, 0), (-1, 0)]
]
ratio = [0.01, 0.01, 0.02, 0.02, 0.07, 0.07, 0.1, 0.1, 0.05]


def spread(x, y, d):
    direction = directions[d]
    now = board[x][y]
    if not now:
        return
    for i in range(9):
        amount = int(now*(ratio[i]))
        nx = x+direction[i][0]
        ny = y+direction[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += amount
        board[x][y] -= amount
    # a
    nx = x+direction[9][0]
    ny = y+direction[9][1]
    if 0 <= nx < n and 0 <= ny < n:
        board[nx][ny] += board[x][y]
    board[x][y] = 0


n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

total = 0
for i in range(n):
    total += sum(board[i])

x, y = n//2, n//2
d = 0
cnt = 1
while True:
    for _ in range(2):
        for c in range(cnt):
            x += dx[d]
            y += dy[d]
            spread(x, y, d)
        d = (d+1) % 4
    # 마지막 줄 한번 더
    if cnt == n-1:
        for c in range(cnt):
            x += dx[d]
            y += dy[d]
            spread(x, y, d)
        break
    cnt += 1

left = 0
for i in range(n):
    left += sum(board[i])

print(total-left)
