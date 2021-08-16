# 시간초과 개빡치는 문제

import sys
from collections import deque
input = sys.stdin.readline

board = []
swan = []
r, c = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(r):
    arr = list(input().strip())
    board.append(arr)
    for j in range(len(arr)):
        if(arr[j] == 'L'):
            swan.append((i, j))

# 해당 위치는 몇 초 후에 전부 녹는지를 저장한 배열
time = [[0 for _ in range(c)] for _ in range(r)]

# 빙하가 녹는 시간대를 time에 저장하고
# 가장 마지막으로 빙하가 녹는 시간이 몇 초인지를 리턴하는 함수
def melt_time_set(board):
    visited = [[0 for _ in range(c)] for _ in range(r)]
    
    # 처음에 바다이거나 백조인 부분
    q = deque()
    for i in range(r):
        for j in range(c):
            if(board[i][j] == '.' or board[i][j] == 'L'):
                q.append((i, j))
                visited[i][j] = 1

    # 마지막으로 빙하가 녹는 시간
    last_time = 0

    # 각 위치의 빙하가 녹는 데 몇 초가 필요한지
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<r and 0<=ny<c):
                if(visited[nx][ny] == 0 and board[nx][ny] != 'L'):
                    # 얼음 부분
                    q.append((nx, ny))
                    time[nx][ny] = time[x][y] + 1
                    visited[nx][ny] = 1
                    last_time = time[nx][ny]

    return last_time

def bfs(start, board, mid, end):
    q = deque()
    q.append(start)
    visited = [[0 for _ in range(c)] for _ in range(r)]
    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<r and 0<=ny<c):
                if(visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    # 백조 1이 백조 2 위치에 도착할 수 있는 경우
                    if(nx == end[0] and ny == end[1]):
                        return 1
                    # 기준 시간초인 mid보다 작은 빙하는 녹아서 이동가능한 것으로 간주
                    if(time[nx][ny] <= mid):
                        q.append((nx, ny))
    return False

# 시간을 기준으로 이분탐색
# mid 초가 지난 후 백조끼리 연결이 가능한지
_min, _max = 0, melt_time_set(board)
answer = _max
while(_min <= _max):
    mid = (_min + _max) // 2
    if(bfs(swan[0], board, mid, swan[1])):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1

print(answer)
