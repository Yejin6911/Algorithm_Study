from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split()) # 행, 열
board = [list(map(int, input().split())) for _ in range(n)]
year = 0

def bfs(x, y):  # dfs -> bfs
    global visited
    visited[x][y] = 1
    q = deque() 
    q.append([x, y])
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny] > 0):
                visited[nx][ny] = 1
                q.append([nx, ny])


def melting(board): # 빙산 녹음
    tempboard = deepcopy(board)
    flag = 0
    for i in range(n):
        for j in range(m):
            if(board[i][j] > 0):
                flag = 1

                if(i-1>=0 and board[i-1][j] == 0):
                    tempboard[i][j] -= 1
                if(j-1>=0 and board[i][j-1] == 0):
                    tempboard[i][j] -= 1
                if(j+1<m and board[i][j+1] == 0):
                    tempboard[i][j] -= 1
                if(i+1<n and board[i+1][j] == 0):
                    tempboard[i][j] -= 1

                if(tempboard[i][j] < 0):
                    tempboard[i][j] = 0
    return tempboard, flag

def check(board):
    global visited
    group = 0
    for i in range(n):
        for j in range(m):
            if(board[i][j] > 0 and visited[i][j] == 0):
                bfs(i, j)
                group += 1
    if(group >= 2):
        return True
    else:
        return False

while(1):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    if(check(board)):
        print(year)
        break
    else:
        board, flag = melting(board)
        year += 1
        if(flag == 0):
            print(0)
            break
