import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split()) # 땅 크기, 인구차이 L명 이상 R명 이하
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
flag = 0

def bfs(x, y, board):
    global visited, flag
    q = deque()
    q.append([x, y])
    location = deque()
    location.append([x, y])
    summ = board[x][y]
    visited[x][y] = 1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<N and 0<=ny<N and visited[nx][ny] == 0):
                if(L <= abs(board[x][y] - board[nx][ny]) <= R):
                    summ += board[nx][ny]
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    location.append([nx, ny])
                    flag = 1
    if(len(location) == 0):
        return board
    avg = summ // len(location)
    for i in range(len(location)):
        board[location[i][0]][location[i][1]] = avg

    return board

cnt = 0
while(1):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if(visited[i][j] == 0):
                board = bfs(i, j, board)
    if(flag == 0):
        print(cnt)
        break
    else:
        cnt += 1
        flag = 0











# nations = [] # 인접하는 나라들
# for i in range(N):
#     for j in range(N-1):
#         nations.append([[i, j], [i, j+1]])
#
# for i in range(N-1):
#     for j in range(N):
#         nations.append([[i, j], [i+1, j]])
#
# while(1):
#     whole = []
#     for i in range(len(nations)):
#         a, b = nations[i] # 인접하는 두 나라 a, b
#         if(L <= abs(board[a[0]][a[1]] - board[b[0]][b[1]]) <= R):
#             if(not(a in whole) and not(b in whole)):
#                 whole.append([a, b])
#             elif(not(a in whole) and b in whole):


