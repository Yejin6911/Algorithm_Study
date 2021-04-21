import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 크기, 말의 개수
color = [list(map(int, input().split())) for _ in range(n)] # 보드 색깔
horseinfo = {} 
board = [[[] for _ in range(n)] for _ in range(n)] 

for i in range(k):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append(i)  # 말의 위치
    horseinfo[i] = [x-1, y-1, d] # 말의 좌표와 방향

dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
        
def changedirection(d): # 방향 바꾸기
    if(d == 1):
        d = 2
    elif(d == 2):
        d = 1
    elif(d == 3):
        d = 4
    else:
        d = 3
    return d

def red(nx, ny, movehorse): # 빨간색
    global horseinfo, board
    board[nx][ny] += movehorse[::-1] # 뒤집어서 올리기
    for i in range(len(movehorse)):
        horseinfo[movehorse[i]][0] = nx
        horseinfo[movehorse[i]][1] = ny

def blue(x, y, h, movehorse): # 파란색
    global horseinfo, board
    horseinfo[h][2] = changedirection(horseinfo[h][2])
    d = horseinfo[h][2]
    nx = x + dx[d] # 거꾸로 좌표
    ny = y + dy[d]
    if(0<=nx<n and 0<=ny<n):
        if(color[nx][ny] == 1): # 빨간색
            red(nx, ny, movehorse)
        elif(color[nx][ny] == 2): # 파란색
            board[x][y] += movehorse
            return x, y
        else: # 흰색
            board[nx][ny] += movehorse
            for i in range(len(movehorse)):
                horseinfo[movehorse[i]][0] = nx
                horseinfo[movehorse[i]][1] = ny
    else: # 범위 벗어나면
        board[x][y] += movehorse
        return x, y
    return nx, ny

def solution():
    cnt = 0
    while(1):
        for h in range(k): # 0번 말 ~ k-1번 말
            x, y, d = horseinfo[h]
            idx = board[x][y].index(h)
            movehorse = board[x][y][idx:] # 리스트
            board[x][y] = board[x][y][:idx] # 말 들어서

            nx = x + dx[d]
            ny = y + dy[d]
            if(0<=nx<n and 0<=ny<n): # 범위 체크
                if(color[nx][ny] == 1): # 빨강
                    red(nx, ny, movehorse)
                elif(color[nx][ny] == 2): # 파랑
                    nx, ny = blue(x, y, h, movehorse)
                else: # 흰
                    board[nx][ny] += movehorse 
                    for i in range(len(movehorse)):
                        horseinfo[movehorse[i]][0] = nx
                        horseinfo[movehorse[i]][1] = ny
            else:
                nx, ny = blue(x, y, h, movehorse)

            if(len(board[nx][ny]) >= 4): # 길이가 4 이상
                print(cnt+1)
                return

        cnt += 1 # 1턴 증가

        if(cnt > 1000):
            print(-1)
            return

solution()