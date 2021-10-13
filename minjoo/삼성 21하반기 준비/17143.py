import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1].append([s, d, z]) # 속력, 이동방향, 크기

dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1] # 위, 아래, 오른쪽, 왼쪽


def move():
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if(len(board[i][j]) > 0):
                s, d, z = board[i][j][0] # 속력, 이동방향, 크기
                x, y = i, j
                for k in range(s):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if(not(0<=nx<r and 0<=ny<c)): # 범위 벗어나면
                        if(d % 2 == 0):
                            d -= 1
                        else:
                            d += 1
                        nx = x + dx[d]
                        ny = y + dy[d]
                    x, y = nx, ny

                # 이미 상어가 있으면
                if(len(temp[x][y]) > 0):
                
                    if(temp[x][y][0][2] < z):
                        temp[x][y] = [[s, d, z]]
                else:
                    temp[x][y] = [[s, d, z]]
    return temp
                
def getshark(idx):
    z_sum = 0
    for i in range(r):
        if(len(board[i][idx]) > 0):
            z_sum += board[i][idx][0][2]
            board[i][idx] = [] # 상어 잡기
            break
    return z_sum

ans = 0
for i in range(c):
    ans += getshark(i)
    board = move()

print(ans)