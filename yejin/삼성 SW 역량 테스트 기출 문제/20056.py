import sys
import copy
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, m, s, d = map(int, input().rstrip().split())
    board[r-1][c-1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def move():
    new_board = copy.deepcopy(board)
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                for _ in range(len(board[x][y])):
                    b = new_board[x][y].pop(0)
                    nx = (x+dx[b[2]]*b[1]) % n
                    ny = (y+dy[b[2]]*b[1]) % n
                    new_board[nx][ny].append(b)
    return new_board


def update():
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) >= 2:
                total_m = 0
                total_s = 0
                total_d = 0
                length = len(board[x][y])
                for b in board[x][y]:
                    m, s, d = b
                    total_m += m
                    total_s += s
                    if d % 2:
                        total_d += 1
                nm = total_m//5
                ns = total_s//length
                if nm == 0:
                    board[x][y] = []
                    pass
                else:
                    if total_d == 0 or total_d == length:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]
                    board[x][y] = []
                    for i in range(4):
                        board[x][y].append([nm, ns, nd[i]])


for _ in range(k):
    board = move()
    update()

result = 0
for x in range(n):
    for y in range(n):
        if board[x][y]:
            for b in board[x][y]:
                result += b[0]

print(result)
