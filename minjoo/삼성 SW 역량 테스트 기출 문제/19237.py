import sys
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 격자 크기, 상어 수, 냄새 지속시간
board = [list(map(int, input().split())) for _ in range(n)] # 격자판
loc_dir = {} # 상어 현재 위치 + 현재 방향
for i in range(n):
    for j in range(n):
        if(board[i][j] != 0):
            board[i][j] = [board[i][j], k]
            loc_dir[board[i][j][0]] = [i, j]
        else:
            board[i][j] = [0, 0]

dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1] # 위, 아래, 왼쪽, 오른쪽

direction = list(map(int, input().split())) # 상어 방향
for i in range(1, m+1):
    loc_dir[i].append(direction[i-1])

priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split()))) # 위, 아래, 왼쪽, 오른쪽을 향할때 우선순위
priority.insert(0, 0)

def scentminus(board):
    for i in range(n):
        for j in range(n):
            if(board[i][j][1] != 0):
                board[i][j][1] -= 1
            else:
                board[i][j] = [0, 0]
    return board


num = m # 살아있는 상어의 수
cnt = 0
while(num > 1):
    board = scentminus(board)
    tempboard = deepcopy(board)
    for i in range(1, m+1): # 1번~m번 상어
        if(loc_dir[i][0] == -1): # 죽은 상어 패스
            continue
        x, y, d = loc_dir[i] # 현재 좌표, 방향
        flag = 0
        for j in range(4):
            nx = x + dx[priority[i][d-1][j]]
            ny = y + dy[priority[i][d-1][j]]
            if(0<=nx<n and 0<=ny<n):
                if(board[nx][ny][0] == 0): # 냄새가 없는 칸
                    flag = 1
                    if(tempboard[nx][ny][0] != 0): # 이미 상어가 있으면
                        # print(tempboard[nx][ny])
                        if(tempboard[nx][ny][0] > i): # 작은 숫자 상어 승
                            tempboard[nx][ny] = [i, k]
                            loc_dir[i] = [nx, ny, priority[i][d-1][j]]
                            loc_dir[tempboard[nx][ny][0]] = [-1, -1, -1] # 큰 숫자 장어 죽음
                            num -= 1
                            break
                        else:
                            loc_dir[i] = [-1, -1, -1] # 현재 숫자 상어 죽음
                            num -= 1
                            break
                    else:
                        tempboard[nx][ny] = [i, k]
                        loc_dir[i] = [nx, ny, priority[i][d-1][j]]
                        break

        if(flag == 0): # 냄새가 없는 칸이 없으면
            for j in range(4):
                nx = x + dx[priority[i][d-1][j]]
                ny = y + dy[priority[i][d-1][j]]
                if(0<=nx<n and 0<=ny<n):
                    if(board[nx][ny][0] == i): # 자신의 냄새가 있는 칸으로
                        tempboard[nx][ny] = [i, k]
                        loc_dir[i] = [nx, ny, priority[i][d-1][j]]
                        break

    board = deepcopy(tempboard)

    cnt += 1
    if(cnt > 1000):
        cnt = -1
        break

print(cnt)