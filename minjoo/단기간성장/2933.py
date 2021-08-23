import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)] # 동굴
n = int(input()) # 막대를 던진 횟수
h = list(map(int, input().split())) # 막대를 던진 높이

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    rq = deque()
    rq.append([x, y])
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<r and 0<=ny<c):
                if(visited[nx][ny] == 0 and board[nx][ny] == 'x'):
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    rq.append([nx, ny])
    return visited, rq

def check(board):
    visited = [[0 for _ in range(c)] for _ in range(r)]
    cnt = 0
    group = deque()
    for i in range(r):
        for j in range(c):
            if(board[i][j] == 'x' and visited[i][j] == 0):
                visited, rq = bfs(i, j, visited)
                if(cnt == 0):
                    group = rq
                cnt += 1
    if(cnt > 1): # 공중에 떠 있는 클러스터가 있다는 말
        return 1, group
    else:
        return 0, group
            
def moving(group):
    global board
    group = list(group)
    # print("group", group)
    
    while(1):
        temp = []
        group.sort(reverse=True, key=lambda x:x[0])
        x, y = group[0]
        if(x<r-1 and board[x+1][y] == '.'):
            for i in range(len(group)):
                x, y = group[i]
                board[x+1][y] = 'x'
                board[x][y] = '.'
                temp.append([x+1, y])
        else:
            break
        group = temp

for i in range(n):
    if(i%2 == 0):
        for j in range(c):
            if(board[r-h[i]][j] == 'x'):
                board[r-h[i]][j] = '.'
                break
    else:
        for j in range(c-1, -1, -1):
            if(board[r-h[i]][j] == 'x'):
                board[r-h[i]][j] = '.'
                break
    flag, group = check(board)
    if(flag):
        moving(group)

for i in range(r):
    for j in range(c):
        print(board[i][j], end='')
    print()

