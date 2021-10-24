import sys
from math import pow
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
n = int(pow(2, N))
board = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def spin(m, board):
    new = [[0]*n for _ in range(n)]
    for i in range(0, n, m):
        for j in range(0, n, m):
            for dx in range(m):
                for dy in range(m):
                    new[i+dx][j+dy] = board[i+m-dy-1][j+dx]
    return new

def bfs(x, y):
    global visited
    q = deque()
    cnt = 1
    q.append([x, y])
    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n and board[nx][ny] > 0 and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
    return cnt



for q in range(Q):
    m = int(pow(2, L[q]))
    board = spin(m, board)
    new = deepcopy(board)
    for i in range(n):
        for j in range(n):
            cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if(0<=nx<n and 0<=ny<n and board[nx][ny] > 0):
                    cnt += 1
            if(cnt < 3 and board[i][j] > 0):
                new[i][j] -= 1
    board = deepcopy(new)

_sum, _max = 0, 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        _sum += board[i][j]
        if(board[i][j] > 0 and visited[i][j] == 0):
            _max = max(_max, bfs(i, j))

print(_sum)
print(_max)




