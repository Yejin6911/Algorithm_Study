import copy
import sys
input = sys.stdin.readline

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def move(shark):
    for i in range(1, 17):
        if not len(fish[i]):
            continue
        x, y = fish[i][0], fish[i][1]
        for _ in range(9):
            nx = x+dx[board[x][y][1]]
            ny = y+dy[board[x][y][1]]
            # 범위 넘어가거나 상어인 경우
            if nx < 0 or nx > 3 or ny < 0 or ny > 3 or (nx == shark[0] and ny == shark[1]):
                # 방향 전환
                if board[x][y][1] == 8:
                    board[x][y][1] = 1
                else:
                    board[x][y][1] += 1
                continue
            # 해당 위치 물고기 있는 경우 서로 자리 변경
            if board[nx][ny]:
                fish[board[nx][ny][0]] = [x, y]
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            fish[i] = [nx, ny]
            break


def dfs(shark, cnt):
    global result, board, fish
    x, y, d = shark[0], shark[1], shark[2]
    # 물고기 이동
    move((x, y))
    # 상어 이동
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            result = max(result, cnt)
            return
        if not board[nx][ny]:
            x, y = nx, ny
            continue
        temp_board = copy.deepcopy(board)
        temp_fish = copy.deepcopy(fish)
        eat = board[nx][ny]
        fish[board[nx][ny][0]] = []
        board[nx][ny] = []
        dfs((nx, ny, eat[1]), cnt+eat[0])
        board, fish = temp_board, temp_fish
        x, y = nx, ny


board = [[], [], [], []]
fish = [0 for _ in range(17)]

for i in range(4):
    row = list(map(int, input().rstrip().split()))
    for j in range(4):
        # [물고기 종류, 방향]
        board[i].append([row[j*2], row[j*2+1]])
        fish[row[j*2]] = [i, j]

result = 0
# x, y, 방향
shark = (0, 0, board[0][0][1])
cnt = board[0][0][0]
fish[board[0][0][0]] = []
board[0][0] = []
dfs(shark, cnt)
print(result)
