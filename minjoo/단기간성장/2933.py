import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)] # 동굴
n = int(input()) # 막대를 던진 횟수
h = list(map(int, input().split())) # 막대를 던진 높이

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    rq = []
    rq.append([x, y]) # 클러스터 좌표 모음
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

def check(board): # 분리된 클러스터 있는지 확인
    visited = [[0 for _ in range(c)] for _ in range(r)]
    cnt = 0
    group = []
    for i in range(r):
        for j in range(c):
            if(board[i][j] == 'x' and visited[i][j] == 0):
                visited, rq = bfs(i, j, visited) # bfs
                rq.sort(reverse=True, key=lambda x:x[0])
                # print("rq", rq)
                # group = rq
                if(rq[0][0] != r-1):
                    group = rq
                cnt += 1

    if(cnt > 1 and group != []): # 클러스터가 2개 이상이고, 공중에 떠 있는 클러스터가 있다는 말
        return 1, group
    else: # 클러스터가 1개
        if('x' in board[r-1]):
            return 0, group
        else:
            return 1, group
            
def moving(group, board):
    while(1):
        tempboard = deepcopy(board)
        temp = []
        x, y = group[0]
        
        if(x<r-1 and board[x+1][y] == '.'):
            for i in range(len(group)):
                x, y = group[i]
                if(tempboard[x+1][y] == 'x' and [x+1, y] not in group):
                    return board
                tempboard[x+1][y] = 'x'
                tempboard[x][y] = '.'
                temp.append([x+1, y])
            board = deepcopy(tempboard)
        else:
            return board
        group = temp

for i in range(n):
    if(i%2 == 0): # 왼쪽에서 화살 던짐
        for j in range(c):
            if(board[r-h[i]][j] == 'x'):
                board[r-h[i]][j] = '.' # 미네랄 파괴
                break 
    else: # 오른쪽에서 화살 던짐
        for j in range(c-1, -1, -1):
            if(board[r-h[i]][j] == 'x'):
                board[r-h[i]][j] = '.' # 미네랄 파괴
                break

    flag, group = check(board) # 분리된 클러스터 확인
    if(flag):
        board = moving(group, board) # 이동
    # for i in range(r):
    #     for j in range(c):
    #         print(board[i][j], end='')

    #     if(i!=r-1):
    #         print()

for i in range(r):
    for j in range(c):
        print(board[i][j], end='')

    if(i!=r-1):
        print()