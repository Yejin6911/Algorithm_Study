import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
virus = []
empty = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if(arr[j] == 2):
            virus.append([i, j]) # 바이러스
        elif(arr[j] == 0):
            empty.append([i, j]) # 빈공간
    board.append(arr)

combis = list(combinations(empty, 3)) # 벽을 세울 수 있는 후보

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(virus, board):
    q = deepcopy(virus)
    visited = [[0 for _ in range(m)] for _ in range(n)]

    while(q):
        temp = []
        while(q):
            x, y = q.pop(0)
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny] == 0):
                    board[nx][ny] = 2
                    visited[x][y] = 1
                    temp.append([nx, ny])
        q = q + temp 

    cnt = 0
    for arr in board:
        cnt += arr.count(0) # 빈공간 수

    return cnt


ans = 0
for idx in range(len(combis)):
    temp = deepcopy(board)
    for c in combis[idx]:
        temp[c[0]][c[1]] = 1 # 벽 세우기

    ans = max(ans, bfs(virus, temp))

print(ans)

