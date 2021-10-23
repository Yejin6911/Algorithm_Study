import copy
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
board = [[[] for _ in range(4)] for _ in range(4)]
fish = [[0, 0] for _ in range(17)]

# board각 자리 [물고기 번호, 방향]
# 상어 번호: 0, 물고기: 1-15
for i in range(4):
    row = list(map(int, input().rstrip().split()))
    for j in range(4):
        a = row[j*2]
        b = row[j*2+1]-1
        fish[a] = [i, j]
        board[i][j] = [a, b]


def dfs(board, fish, total):
    board, fish = moveFish(board, fish)
    shark = fish[0]
    x, y = shark
    d = board[x][y][1]
    check = False
    while True:
        nx = x+dir[d][0]
        ny = y+dir[d][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if len(board[nx][ny]):
                check = True
                new_board = copy.deepcopy(board)
                new_fish = copy.deepcopy(fish)
                # 잡아먹힌 물고기 위치 처리
                new_fish[new_board[nx][ny][0]] = [-1, -1]
                # 상어 위치 변경
                new_fish[0] = [nx, ny]
                # 상어 위치 및 방향 변경
                new_board[nx][ny] = [0, new_board[nx][ny][1]]
                new_board[shark[0]][shark[1]] = []
                dfs(new_board, new_fish, total + board[nx][ny][0])
            x, y = nx, ny
        else:
            break
    # 더이상 이동 불가한 경우
    if not check:
        global answer
        answer = max(answer, total)
        return


def moveFish(board, fish):
    new_board = copy.deepcopy(board)
    new_fish = copy.deepcopy(fish)
    for i in range(1, 17):
        x, y = new_fish[i]
        # 잡아먹힌 경우
        if x == -1 and y == -1:
            continue
        cnt = 0
        while True:
            d = new_board[x][y][1]
            # 모든 방향 이동 불가한 경우
            if cnt == 8:
                break
            nx = x+dir[d][0]
            ny = y+dir[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                # 상어인경우
                if len(new_board[nx][ny]) and new_board[nx][ny][0] == 0:
                    new_board[x][y][1] = (new_board[x][y][1]+1) % 8
                    cnt += 1
                else:
                    # 자리바꾸기
                    temp = new_board[nx][ny]
                    # 바꾸려는 위치에 물고기 있는 경우
                    if len(temp):
                        new_fish[temp[0]] = [x, y]
                    new_fish[i] = [nx, ny]
                    new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                    break
            else:
                new_board[x][y][1] = (new_board[x][y][1]+1) % 8
                cnt += 1
    return new_board, new_fish


# 첫번째 먹히는 물고기 처리
a, b = board[0][0]
fish[0] = [0, 0]
board[0][0] = [0, b]
fish[a] = [-1, -1]
global answer
answer = a
dfs(board, fish, answer)
print(answer)
