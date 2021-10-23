import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# 블록그룹 찾기
def bfs(x, y, color):
    global visited
    rainbow = 0
    q = deque()
    index = deque()
    rainbow = deque()
    q.append([x, y])
    index.append([x, y])

    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0):
                if(board[nx][ny] != -1):
                    if(board[nx][ny] == color):
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                        index.append([nx, ny])
                    elif(board[nx][ny] == 0):
                        rainbow.append([nx, ny])
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                        index.append([nx, ny])
        
    return index, rainbow

def gravity(board):
    for i in range(n):
        for j in range(1, n):
            if(board[j][i] == '*'): # 빈공간이면
                x, y = j, i
                while(x >= 1):
                    if(board[x-1][y] == -1):
                        break
                    if(board[x-1][y] != '*'):
                        temp = board[x][y]
                        board[x][y] = board[x-1][y]
                        board[x-1][y] = temp
                    x, y = x-1, y
                
    return board

def spin(board):
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = board[j][n-i-1]

    return new

score = 0
while(1):
    visited = [[0]*n for _ in range(n)]
    _max = 0
    max_data = [] # 후보들

    for i in range(n):
        for j in range(n):
            if(visited[i][j] == 0):
                if(board[i][j] != -1 and board[i][j] != 0 and board[i][j] != '*'): # 일반 블록
                    index, rainbow = bfs(i, j, board[i][j])
                    for k in range(len(rainbow)):
                        visited[rainbow[k][0]][rainbow[k][1]] = 0
                    if(len(index) < 2):
                        continue

                    if(len(index) > _max):
                        _max = len(index)
                        max_data = [[len(rainbow), i, j, index]]
                        
                    elif(len(index) == _max):
                        max_data.append([len(rainbow), i, j, index])

    if(len(max_data) == 0):
        break
    
    if(len(max_data) > 1):
        max_data = sorted(max_data, reverse=True, key = lambda x:(x[0], x[1], x[2]))
    index = max_data[0][3]
    
    for i in range(len(index)):
        x, y = index[i]
        board[x][y] = '*'
    score += len(index)*len(index)

    board = gravity(board)
    board = spin(board)
    board = gravity(board)

print(score)