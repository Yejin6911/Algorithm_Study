import sys
import copy
input = sys.stdin.readline


# 미세먼지 확산
def spread():
    temp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] == -1:
                temp[x][y] = -1
                continue
            elif board[x][y] > 0:
                cnt = 0
                amount = board[x][y]//5
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        temp[nx][ny] += amount
                        cnt += 1
                temp[x][y] += (board[x][y]-amount*cnt)
    return temp


# 공기청정기 작동
def clean(d):
    temp = copy.deepcopy(board)
    direction = D[d]
    x = cleaner[d][0]
    y = cleaner[d][1]+1
    # 처음위치 0으로 만들어줌
    board[x][y] = 0
    finish = (x, y-1)
    for i in range(4):
        while True:
            nx = x+dx[direction[i]]
            ny = y+dy[direction[i]]
            if nx == finish[0] and ny == finish[1]:
                return
            if 0 <= nx < r and 0 <= ny < c:
                board[nx][ny] = temp[x][y]
            else:
                break
            x, y = nx, ny


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 바람 부는 방향
D = [[3, 0, 2, 1], [3, 1, 2, 0]]

r, c, t = map(int, input().rstrip().split())
board = []
cleaner = []
for i in range(r):
    row = list(map(int, input().rstrip().split()))
    board.append(row)
    for j in range(len(row)):
        if row[j] == -1:
            cleaner.append((i, j))
# 윗부분이 앞으로 오게
cleaner.sort()

for i in range(t):
    board = spread()
    for i in range(2):
        clean(i)
result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
