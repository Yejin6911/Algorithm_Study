import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 격자 크기, 명령 개수
board = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
cloud = deque(cloud)

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

move = [list(map(int, input().split())) for _ in range(m)]

for idx in range(m):
    # 구름 이동
    d, s = move[idx]
    new_cloud = deque()
    for i in range(len(cloud)):
        x, y = cloud[i]
        nx = x + dx[d]*s
        ny = y + dy[d]*s
       
        nx = nx % n
        ny = ny % n

        new_cloud.append([nx, ny])
    cloud = deepcopy(new_cloud)
 
    # 비가 내림
    for i in range(len(cloud)):
        board[cloud[i][0]][cloud[i][1]] += 1
    
    # 물의 양 증가
    for i in range(len(cloud)):
        cnt = 0
        x, y = cloud[i]
        for j in range(4):
            nx = x + dx2[j]
            ny = y + dy2[j]
            if(0<=nx<n and 0<=ny<n and board[nx][ny] > 0):
                cnt += 1
        board[x][y] += cnt

    # 구름 생김 + 물 증발
    new_cloud = deque()
    for i in range(n):
        for j in range(n):
            if(board[i][j] >= 2 and not([i, j] in cloud)):
                new_cloud.append([i, j])
                board[i][j] -= 2
    cloud = deepcopy(new_cloud)

result = 0
for i in range(n):
    result += sum(board[i])

print(result)