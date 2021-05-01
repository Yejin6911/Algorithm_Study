import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 한변의 크기, 색상의 개수

board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def find(x, y, color):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([x, y])
    cnt = 1
    rainbow = 0
    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0):
                if(board[nx][ny] == 0 or board[nx][ny] == color):
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    if(board[nx][ny] == 0):
                        rainbow += 1
    return cnt, rainbow, visited

max_cnt = 0
candidates = []
for i in range(n):
    for j in range(n):
        if(board[i][j] > 0):
            cnt, rainbow, visited = find(i, j, board[i][j])
            if(max_cnt < cnt):
                max_cnt = cnt
                candidates = [rainbow, i, j, visited]
            elif(max_cnt == cnt):
                candidates.append([rainbow, i, j, visited])

candidates.sort(reverse=True, key = lambda x:(x[0], x[1], x[2]))
v = candidates[0][3]
for i in range(n):
    for j in range(n):
        if(v[i][j]):
            board[i][j] = -2 # 제거

# 중력 작용
for i in range(n):
    nums = []
    for j in range(n):
        if(board[j][i] == -1):
            nums.append(-1)
            
            break
        if(board[j][i] != -2):
            nums.append(board[j][i])

