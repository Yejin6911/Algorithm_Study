from collections import deque
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def find(x, y):
    group = [(x, y)]
    included[x][y] = 1
    color = board[x][y]
    queue = deque()
    queue.append((x, y))
    r_cnt = 0  # 무지개블록수
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n and 0 <= ny < n):
                # 무지개 블록
                if board[nx][ny] == 0 and (nx, ny) not in group:
                    r_cnt += 1
                    queue.append((nx, ny))
                    group.append((nx, ny))
                # 같은 색의 블록
                elif board[nx][ny] == color and not included[nx][ny]:
                    included[nx][ny] = 1
                    queue.append((nx, ny))
                    group.append((nx, ny))
    group.sort()
    for x, y in group:
        if board[x][y] != 0:
            s = (x, y)
            break
    return s, r_cnt, group


def erase(group):
    for x, y in group:
        board[x][y] = -2
    global total
    total += (len(group)**2)


def spin():
    new_board = copy.deepcopy(board)
    for j in range(n-1, -1, -1):
        for i in range(n):
            board[n-1-j][i] = new_board[i][j]


def move():
    # 중력 작용
    for y in range(n):
        for x in range(n-2, -1, -1):
            if board[x][y] < 0:
                continue
            else:
                if board[x+1][y] == -2:
                    temp = x+1
                    while temp+1 < n:
                        if board[temp+1][y] == -2:
                            temp += 1
                        else:
                            break
                    board[temp][y], board[x][y] = board[x][y], -2


n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
global total
total = 0

while True:
    included = [[0]*n for _ in range(n)]
    candidates = []
    for i in range(n):
        for j in range(n):
            # 일반 블록일 때
            if board[i][j] > 0 and not included[i][j]:
                s, r_cnt, group = find(i, j)
                if len(group) > 1:
                    candidates.append([group, r_cnt, s])
    if not len(candidates):
        break
    candidates.sort(key=lambda x: (-len(x[0]), -x[1], -x[2][0], -x[2][1]))
    erase(candidates[0][0])
    move()
    spin()
    move()
print(total)
