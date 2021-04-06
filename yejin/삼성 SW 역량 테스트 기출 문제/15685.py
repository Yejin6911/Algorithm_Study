import sys

input = sys.stdin.readline

board = [[0]*101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input().rstrip())
# 내가 푼 방법 - 포함되는 좌표 저장
for i in range(n):
    x, y, d, g = map(int, input().rstrip().split())
    dc = [(x, y)]
    board[y][x] = 1
    for i in range(g+1):
        if i == 0:
            start = dc[-1]
            nx = start[0]+dx[d]
            ny = start[1]+dy[d]
            board[ny][nx] = 1
            dc.append((nx, ny))
        else:
            for j in range(len(dc)-2, -1, -1):
                start = dc[-1]
                diff_x = dc[j][0]-dc[j+1][0]
                diff_y = dc[j][1]-dc[j+1][1]
                if diff_x == 1 and diff_y == 0:
                    d = 3
                elif diff_x == 0 and diff_y == 1:
                    d = 2
                elif diff_x == -1 and diff_y == 0:
                    d = 1
                else:
                    d = 0
                nx = start[0] + dx[d]
                ny = start[1] + dy[d]
                board[ny][nx] = 1
                dc.append((nx, ny))

# 방법 2 - 이동방향 저장
for _ in range(n):
    x, y, d, g = map(int, input().rstrip().split())
    board[y][x] = 1
    move = [d]
    for i in range(g):
        temp = []
        for j in range(len(move)):
            temp.append((move[-j-1]+1) % 4)
        move += temp
    for i in move:
        nx = x+dx[i]
        ny = y+dy[i]
        board[ny][nx] = 1
        x, y = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1
print(result)
