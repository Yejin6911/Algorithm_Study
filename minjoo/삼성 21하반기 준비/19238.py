import sys
from collections import deque
input = sys.stdin.readline

n, m, oil = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split()) # 운전을 시작하는 행 번호와 열 번호
x -= 1
y -= 1
start = []
end = []
for _ in range(m):
    arr = list(map(int, input().split()))
    start.append([arr[0]-1, arr[1]-1])
    end.append([arr[2]-1, arr[3]-1])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def findclient(x, y):
    if([x, y] in start):
        return 0, x, y

    visited = [[0]*n for _ in range(n)]
    q = []
    q.append([x, y])
    cnt = 0
    nextxy = []
    while(q):
        temp = []
        cnt += 1
        while(q):
            x, y = q.pop(0)
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n):
                    if(board[nx][ny] == 0 and visited[nx][ny] == 0):
                        visited[nx][ny] = 1
                        if([nx, ny] in start):
                            nextxy.append([nx, ny])
                        else:
                            temp.append([nx, ny])
        if(nextxy):
            nextxy.sort(key = lambda x:(x[0], x[1]))
            return cnt, nextxy[0][0], nextxy[0][1]
        q = q + temp

    return -1, -1, -1

def goend(x, y, ex, ey):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([x, y])
    cnt = 0
    while(q):
        temp = deque()
        cnt += 1
        while(q):
            x, y = q.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx<n and 0<=ny<n):
                    if(board[nx][ny] == 0 and visited[nx][ny] ==0):
                        visited[nx][ny] = 1
                        if([nx, ny] == [ex, ey]):
                            return cnt
                        temp.append([nx, ny])
        q = q + temp
    return -1


while(start):
    far1, nx, ny = findclient(x, y)

    oil -= far1
    if(far1 == -1 or oil < 0):
        oil = -1
        break

    idx = start.index([nx, ny])
    far2 = goend(nx, ny, end[idx][0], end[idx][1])
    
    oil -= far2
    if(far2 == -1 or oil < 0):
        oil = -1
        break

    oil += far2 * 2

    x, y = end[idx][0], end[idx][1]

    start.pop(idx)
    end.pop(idx)


print(oil)