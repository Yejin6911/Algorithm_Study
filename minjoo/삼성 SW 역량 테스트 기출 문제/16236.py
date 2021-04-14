import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(board[i][j] == 9):
            x, y = i, j # 아기상어 위치

size = 2 # 아기상어 크기
board[x][y] = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # 북서남동

result = 0
weight = 0
def bfs(x, y):
    global visited, board, result, weight, size
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append([x, y, 0])
    eat = []
    
    while(q):
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n and visited[nx][ny] == 0): # 범위체크
                if(board[nx][ny] == 0 or board[nx][ny] == size):
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt+1]) # 통과
                elif(0 < board[nx][ny] < size):
                    visited[nx][ny] = 1
                    eat.append([nx, ny, cnt+1]) # 먹는 후보
    

    if(len(eat) > 0):
        eat.sort(key=lambda x: (x[2], x[0], x[1])) # 거리순, 위쪽 왼쪽 순
        
        x, y = eat[0][0], eat[0][1]
        weight += 1
        board[x][y] = 0
        if(weight == size):
            weight -= size
            size += 1
            
        result += eat[0][2]
        return x, y
    else:
        return -1, -1
    
while(1):
    x, y = bfs(x, y)
    if(x == -1):
        print(result)
        break
    

                



