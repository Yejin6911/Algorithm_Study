#pypy로 제출
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

for i in range(r):
    if(board[i][0] == -1):
        cleaner.append([i, 0]) # 공기청정기 좌표

def spread():
    global board
    op = []
    for i in range(r):
        for j in range(c):
            if(board[i][j] > 4 and board[i][j] != -1):
                value = board[i][j] // 5
                cnt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if(0<=ni<r and 0<=nj<c and not([ni, nj] in cleaner)): # 범위체크
                        cnt += 1
                        op.append([ni, nj, value])
                op.append([i, j, -cnt*value])
    for i in range(len(op)):
        board[op[i][0]][op[i][1]] += op[i][2]
        if(board[op[i][0]][op[i][1]] < 0):
            board[op[i][0]][op[i][1]] = 0

def cleaning_clock():
    global board
    x = cleaner[0][0] + dx[0]
    y = cleaner[0][1] + dy[0]
    temp = board[x][y]
    board[x][y] = 0
    for i in range(4):
        while(0<=x<r and 0<=y<c):
            nx = x + dx[i] # 다음좌표
            ny = y + dy[i] # 다음좌표
            if(0<=nx<r and 0<=ny<c):
                temp2 = board[nx][ny]
                if([nx, ny] in cleaner):
                    return
                else:
                    board[nx][ny] = temp
                temp = temp2
                x, y = nx, ny
            else:
                break
       
 
def cleaning_clock_2():
    global board
    x = cleaner[1][0] + dx[0]
    y = cleaner[1][1] + dy[0]
    temp = board[x][y]
    board[x][y] = 0
    idx = [0, 3, 2, 1]
    for i in idx:
        while(0<=x<r and 0<=y<c):
            nx = x + dx[i] # 다음좌표
            ny = y + dy[i] # 다음좌표
            if(0<=nx<r and 0<=ny<c):
                temp2 = board[nx][ny]
                if([nx, ny] in cleaner):
                    return
                else:
                    board[nx][ny] = temp
                temp = temp2
                x, y = nx, ny
            else:
                break

for _ in range(t):
    spread()
    cleaning_clock()
    cleaning_clock_2()


# print(board)
result = 0
for i in range(r):
    for j in range(c):
        if(board[i][j] != -1):
            result += board[i][j]
print(result)

        


