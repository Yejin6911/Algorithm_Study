import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
virus = []
empty = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if(line[j] == 2):
            virus.append([i, j])
        elif(line[j] == 0):
            empty.append([i, j])
    board.append(line)

candidate = list((combinations(empty, 3)))

def bfs(virus, tempboard):
    q = deepcopy(virus)
    visited = [[0]*m for _ in range(n)]
    while(q):
        temp = []
        while(q):
            x, y = q.pop(0)
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<m and tempboard[nx][ny] == 0 and visited[nx][ny] == 0):
                    tempboard[nx][ny] = 2
                    visited[nx][ny] = 1
                    temp.append([nx, ny])
        q = q + temp

    cnt = 0
    for line in tempboard:
        cnt += line.count(0)
    return cnt

result = 0
for cs in candidate:
    tempboard = deepcopy(board)
    for c in cs:
        tempboard[c[0]][c[1]] = 1
    result = max(result, bfs(virus, tempboard))

print(result)