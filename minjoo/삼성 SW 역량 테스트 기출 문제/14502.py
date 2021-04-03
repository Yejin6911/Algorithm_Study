import sys
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

max_result = 0

def bfs():
    global max_result
    copy = deepcopy(board)
    result = 0
    virus = []
    for i in range(n):
        for j in range(m):
            if(copy[i][j] == 2):
                virus.append([i, j])
    while(virus):
        a, b = virus.pop(0)
        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            if(0<=ax<n and 0<=ay<m):
                if(copy[ax][ay] == 0):
                    copy[ax][ay] = 2
                    virus.append([ax, ay])
    for i in copy:
        for j in i:
            if(j == 0):
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if(cnt == 3):
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 0):
                board[i][j] = 1
                wall(cnt + 1)
                board[i][j] = 0

wall(0)
print(max_result)