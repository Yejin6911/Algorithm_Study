import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def move(idx):
    x, y, d = horse[idx]
    nx = x+dx[d]
    ny = y+dy[d]
    # 파란색 또는 범위 벗어나는 경우
    if (nx < 0 or nx >= n or ny < 0 or ny >= n) or board[nx][ny] == 2:
        # 방향 변경
        if horse[idx][2] % 2:
            horse[idx][2] += 1
            d = horse[idx][2]
        else:
            horse[idx][2] -= 1
            d = horse[idx][2]
        nx = x+dx[d]
        ny = y+dy[d]
    # 또 파란색이거나 범위 벗어나는 경우
    if (nx < 0 or nx >= n or ny < 0 or ny >= n) or board[nx][ny] == 2:
        pass
    else:
        now_idx = position[x][y].index(idx)
        # 흰색칸
        if board[nx][ny] == 0:
            for h in position[x][y][now_idx: len(position[x][y])]:
                horse[h][0], horse[h][1] = nx, ny
            position[nx][ny] += position[x][y][now_idx:]
            position[x][y] = position[x][y][:now_idx]
        # 빨간색칸
        elif board[nx][ny] == 1:
            for h in position[x][y][now_idx: len(position[x][y])]:
                horse[h][0], horse[h][1] = nx, ny
            temp = position[x][y][now_idx:]
            temp.reverse()
            position[nx][ny] += temp
            position[x][y] = position[x][y][:now_idx]
    # 4개 쌓인 부분 있는지 확인
    for r in position:
        for c in r:
            if len(c) >= 4:
                return False
    return True


n, k = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 말 위치
position = [[[] for _ in range(n)] for _ in range(n)]
# 말 정보
horse = []
for i in range(k):
    r, c, d = map(int, input().rstrip().split())
    horse.append([r-1, c-1, d])
    position[r-1][c-1].append(i)

turn = 1
while True:
    if turn > 1000:
        turn = -1
        break
    for i in range(k):
        keep = move(i)
        # 4개이상 쌓인 경우 break
        if keep == False:
            break
    if keep:
        turn += 1
    else:
        break

print(turn)
