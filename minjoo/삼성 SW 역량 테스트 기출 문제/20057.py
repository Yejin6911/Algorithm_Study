import sys
from copy import deepcopy
import math
input = sys.stdin.readline

n = int(input()) # 격자의 크기
board = []
original = 0 # 원래 모래 수
for _ in range(n):
    temp = list(map(int, input().split()))
    original += sum(temp)
    board.append(temp)

def spread(x, y, board, dx, dy, p): # y좌표, 격자
    sand = board[x][y]
    board[x][y] = 0
    left = sand
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<n and 0<=ny<n):
            board[nx][ny] += int((sand * p[i]))
        left -= int(sand * p[i])
    return left, board

def spread_left(x, y, board):
    dx = [-1, -2, -1, -1, 0, 1, 2, 1, 1] # (위)7 2 1, 10, 5 (아래) 7 2 1 10
    dy = [0, 0, 1, -1, -2, 0, 0, 1, -1]
    p = [0.07, 0.02, 0.01, 0.1, 0.05, 0.07, 0.02, 0.01, 0.1]
    left, board = spread(x, y, board, dx, dy, p)
    nx, ny = x, y-1
    if(0<=nx<n and 0<=ny<n):
        board[nx][ny] += left
    return board

def spread_right(x, y, board):
    dx = [-1, -2, -1, -1, 0, 1, 2, 1, 1] # (위)7 2 1, 10, 5 (아래) 7 2 1 10
    dy = [0, 0, -1, 1, 2, 0, 0, -1, 1]
    p = [0.07, 0.02, 0.01, 0.1, 0.05, 0.07, 0.02, 0.01, 0.1]
    left, board = spread(x, y, board, dx, dy, p)
    nx, ny = x, y+1
    if(0<=nx<n and 0<=ny<n):
        board[nx][ny] += left
    return board

def spread_up(x, y, board):
    dx = [0, 0, 1, -1, -2, -1, 0, 1, 0]
    dy = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
    p = [0.02, 0.07, 0.01, 0.1, 0.05, 0.1, 0.07, 0.01, 0.02]
    left, board = spread(x, y, board, dx, dy, p)
    nx, ny = x-1, y
    if(0<=nx<n and 0<=ny<n):
        board[nx][ny] += left
    return board

def spread_down(x, y, board):
    dx = [0, 0, -1, 1, 2, 0, 0, -1, 1]
    dy = [-2, -1, -1, -1, 0, 1, 2, 1, 1]
    p = [0.02, 0.07, 0.01, 0.1, 0.05, 0.07, 0.02, 0.01, 0.1]
    left, board = spread(x, y, board, dx, dy, p)
    nx, ny = x+1, y
    if(0<=nx<n and 0<=ny<n):
        board[nx][ny] += left
    return board

length = 1
cnt = 1
dx2 = [0, 1, 0, -1]
dy2 = [-1, 0, 1, 0]
def move(x, y): # 시작점
    global length, cnt, board
    while(1):
        for i in range(4):
            if(cnt == 3):
                length += 1
                cnt = 1
            for _ in range(length):
                if(x == 0 and y == 0):
                    board = spread_left(0, 0, board)
                    return
                nx = x + dx2[i]
                ny = y + dy2[i]
                    
                if(i == 0): # 왼쪽
                    board = spread_left(nx, ny, board)
                elif(i == 1): # 아래
                    board = spread_down(nx, ny, board)
                elif(i == 2): # 오른쪽
                    board = spread_right(nx, ny, board)
                else: # 위
                    board = spread_up(nx, ny, board)
                x, y = nx, ny
                
            cnt += 1
          
move(n//2, n//2)

leftsum = 0
for i in range(n):
    for j in range(n):
        leftsum += board[i][j]
print(original - leftsum)