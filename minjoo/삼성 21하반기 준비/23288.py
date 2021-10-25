from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0 # 현재 주사위 위치

front = 5
middle = [6, 3, 1, 4]
back = 2
num = middle[0] # 바닥면

d = 0 # 방향

def bfs(x, y, num):
    visited = [[0]*m for _ in range(n)]
    cnt = 1
    q = deque()
    q.append([x, y])
    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny] == num):
                cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return cnt
                
score = 0

for _ in range(k):
    nx = x + dx[d]
    ny = y + dy[d]

    if(not(0<=nx<n and 0<=ny<m)):
        if(d == 0):
            d = 2
        elif(d == 1):
            d = 3
        elif(d == 2):
            d = 0
        else:
            d = 1
        nx = x + dx[d]
        ny = y + dy[d]

    if(d == 0):
        middle = middle[1:] + middle[:1]
    elif(d == 1):
        temp_back = back
        temp_front = front
        front = middle[2]
        back = middle[0]
        middle[0] = temp_front
        middle[2] = temp_back
    elif(d == 2):
        middle = middle[3:] + middle[:3]
    else:
        temp_back = back
        temp_front = front
        front = middle[0]
        back = middle[2]
        middle[0] = temp_back
        middle[2] = temp_front
    
    num = middle[0] # 바닥면

    cnt = bfs(nx, ny, board[nx][ny])

    score += cnt * board[nx][ny]

    if(num > board[nx][ny]):
        d += 1
    elif(num < board[nx][ny]):
        d -= 1
    else:
        pass

    if(d >= 0):
        d = d % 4
    else:
        while(d < 0):
            d += 4
    

    x, y = nx, ny
print(score)

    