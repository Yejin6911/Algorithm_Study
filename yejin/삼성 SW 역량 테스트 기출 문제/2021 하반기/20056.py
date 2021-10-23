import copy

n, m, k = map(int, input().rstrip().split())
board = [[[] for _ in range(n)] for _ in range(n)]
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(m):
    r, c, m, s, d = map(int, input().rstrip().split())
    board[r-1][c-1].append((m, s, d))

for _ in range(k):
    new_board = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(board[x][y]):
                for b in board[x][y]:
                    m, s, d = b
                    nx = (x + dir[d][0]*s) % n  # 좌표순환
                    ny = (y + dir[d][1]*s) % n
                    new_board[nx][ny].append((m, s, d))
    for x in range(n):
        for y in range(n):
            if len(new_board[x][y]) > 1:
                total_m = 0
                total_s = 0
                total_d = []
                for b in new_board[x][y]:
                    total_m += b[0]
                    total_s += b[1]
                    total_d.append(b[2] % 2)
                new_m = total_m//5
                new_s = total_s//len(new_board[x][y])
                if new_m == 0:
                    new_board[x][y] = []
                else:
                    if sum(total_d) == 0 or sum(total_d) == len(new_board[x][y]):
                        new_d = [0, 2, 4, 6]
                    else:
                        new_d = [1, 3, 5, 7]
                    new_board[x][y] = [
                        (new_m, new_s, new_d[0]),
                        (new_m, new_s, new_d[1]),
                        (new_m, new_s, new_d[2]),
                        (new_m, new_s, new_d[3])
                    ]
    board = new_board

total = 0
for x in range(n):
    for y in range(n):
        if len(board[x][y]):
            for b in board[x][y]:
                total += b[0]
print(total)
