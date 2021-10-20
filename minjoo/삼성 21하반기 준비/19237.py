import sys
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []
shark = {i:[] for i in range(1, m+1)}

for i in range(n):
    arr = list(map(int, input().split()))
    temp = []
    for j in range(n):
        if(arr[j] != 0):
            shark[arr[j]] = [i, j]
            temp.append([arr[j], k])
        else:
            temp.append([0, 0])
    board.append(temp)

direction = list(map(int, input().split()))
for i in range(m):
    shark[i+1].append(direction[i])

dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1] # 위, 아래, 왼쪽, 오른쪽
priority = [[] for _ in range(m+1)]
for i in range(m):
    for j in range(4):
        arr = list(map(int, input().split()))
        priority[i+1].append(arr)

dead_shark = []

def shark_move():
    global board
    newboard = deepcopy(board)
    for i in range(1, m+1): # 상어 한마리씩 이동
        x, y, d = shark[i]
        if(i in dead_shark): # 죽은 상어면
            continue
        direc = priority[i][d-1] # 방향 우선순위
        flag = 0

        for j in range(4): # 인접한 빈공간 탐색
            nx = x + dx[direc[j]]
            ny = y + dy[direc[j]]
            if(0<=nx<n and 0<=ny<n and board[nx][ny] == [0, 0]):
                if(newboard[nx][ny] != [0, 0]): # 이미 상어가 있다면
                    if(newboard[nx][ny][0] < i): # 원래 있던 상어가 더 작은 수면
                        shark[i] = [-1, -1, -1] # 잡아먹힘
                        flag = 1
                        if(i not in dead_shark):
                            dead_shark.append(i)
                        break
                    else: # 지금 상어가 더 작은 수면
                        dead = newboard[nx][ny][0]
                        if(dead not in dead_shark):
                            dead_shark.append(dead)
                        shark[dead] = [-1, -1, -1]
                        newboard[nx][ny] = [i, k]
                        shark[i] = [nx, ny, direc[j]]
                        flag = 1
                        break
                else: # 상어가 없으면
                    newboard[nx][ny] = [i, k]
                    shark[i] = [nx, ny, direc[j]]
                    flag = 1
                    break
        if(flag == 0): # 인접한 칸이 없으면
            for j in range(4):
                nx = x + dx[direc[j]]
                ny = y + dy[direc[j]]
                if(0<=nx<n and 0<=ny<n and board[nx][ny][0] == i):
                    newboard[nx][ny] = [i, k]
                    shark[i] = [nx, ny, direc[j]]
                    break
    # 냄새 -1
    for i in range(n):
        for j in range(n):
            if(newboard[i][j][1] != 0):
                num = newboard[i][j][0]
                if([i, j] != [shark[num][0], shark[num][1]]): # 현재 자리가 아니면
                    newboard[i][j][1] -= 1
                if(newboard[i][j][1] == 0): # 냄새 다 없어졌으면
                    newboard[i][j][0] = 0
    
    board = deepcopy(newboard)

cnt = 0
while(1):
    shark_move()
    cnt += 1
    if(len(dead_shark) == (m-1)):
        print(cnt)
        break
    if(cnt >= 1000):
        print(-1)
        break