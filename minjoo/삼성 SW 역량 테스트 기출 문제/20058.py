# pypy로 제출
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split()) # 격자 크기, 파이어스톰 횟수
board = [list(map(int, input().split())) for _ in range(2**n)]
step = list(map(int, input().split())) # L1~Lq
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def rotate(b): # 시계방향 90도 회전
    temp_b = deepcopy(b)
    for i in range(len(b)):
        for j in range(len(b)):
            temp_b[j][len(b)-i-1] = b[i][j]
    return temp_b

def bfs(x, y): # 얼음 덩어리 크기 구하기
    global visited
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<2**n and 0<=ny<2**n and visited[nx][ny] == 0 and board[nx][ny] != 0):
                cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return cnt

for s in step:
    for i in range(0, 2**n, 2**s):
        for j in range(0, 2**n, 2**s):
            line = board[i:i+2**s]
            tempb = []
            for li in line:
                tempb.append(li[j:j+2**s])
            tempb = rotate(tempb)
            for d in range(2**s):
                for p in range(2**s):
                    board[i+d][j+p] = tempb[d][p]

    tempboard = deepcopy(board)
    for i in range(2**n):
        for j in range(2**n):
            if(board[i][j] <= 0):
                continue
            cnt = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if(0<=ni<2**n and 0<=nj<2**n and board[ni][nj] > 0):
                    cnt += 1
            if(cnt < 3):
                tempboard[i][j] -= 1
    board = deepcopy(tempboard)

summ = 0
for i in range(2**n):
    for j in range(2**n):
        summ += board[i][j]

maxx = 0
visited = [[0]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if(visited[i][j] == 0 and board[i][j] != 0):
            maxx = max(maxx, bfs(i, j))

print(summ)
print(maxx)


