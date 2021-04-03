import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 청소 구역
r, c, d = map(int, input().split()) # 청소기 좌표, 방향

board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서

def solution():
    global r, c, d, board
    cnt = 0
    while(1):
        change = 0
        if(board[r][c] == 0):
            board[r][c] = 2 # 청소
            cnt += 1
        for i in range(1, 5):
            nx = r + dx[d-i] # 다음 x좌표
            ny = c + dy[d-i] # 다음 y좌표
            if(0<=nx<n and 0<=ny<m):
                if(board[nx][ny] == 0): # 빈칸이면
                    r, c = nx, ny
                    change = 1
                    d -= i
                    if(d < 0):
                        d += 4
                    break
        if(change == 0): # 네 방향 모두 청소가 되어있거나 벽이면
            nx = r - dx[d]
            ny = c - dy[d]
            if(board[nx][ny] == 1):
                break
            else:
                r, c = nx, ny
    return cnt

print(solution())



