import sys
input = sys.stdin.readline


dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


def move(p):
    x, y, d = now[p]
    nx = x+dir[d][0]
    ny = y+dir[d][1]
    if (0 <= nx < n and 0 <= ny < n) and 0 <= board[nx][ny] < 2:
        index = piece[x][y].index(p)
        temp = piece[x][y][index:]
        # 흰색
        if board[nx][ny] == 0:
            # 움직이는 말들 위치 변경
            piece[x][y] = piece[x][y][:index]
            piece[nx][ny].extend(temp)
            for i in temp:
                now[i][0], now[i][1] = nx, ny
        # 빨간색
        elif board[nx][ny] == 1:
            piece[x][y] = piece[x][y][:index]
            temp.reverse()
            piece[nx][ny].extend(temp)
            for i in temp:
                now[i][0], now[i][1] = nx, ny
        return len(piece[nx][ny])
    # 파란색 or 범위 벗어난 경우
    else:
        if d % 2:
            now[p][2] = d+1
            d += 1
        else:
            now[p][2] = d-1
            d -= 1
        nx = x+dir[d][0]
        ny = y+dir[d][1]
        if (0 <= nx < n and 0 <= ny < n) and 0 <= board[nx][ny] < 3:
            index = piece[x][y].index(p)
            temp = piece[x][y][index:]
            # 흰색인 경우
            if board[nx][ny] == 0:
                # 움직이는 말들 위치 변경
                piece[x][y] = piece[x][y][:index]
                piece[nx][ny].extend(temp)
                for i in temp:
                    now[i][0], now[i][1] = nx, ny
            # 빨간색
            elif board[nx][ny] == 1:
                piece[x][y] = piece[x][y][:index]
                temp.reverse()
                piece[nx][ny].extend(temp)
                for i in temp:
                    now[i][0], now[i][1] = nx, ny
            return len(piece[nx][ny])
        # 또 파란색이거나 범위 벗어난 경우
        return -1


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
piece = [[[] for _ in range(n)] for _ in range(n)]
now = [0]  # 말의 현재 위치


for i in range(1, k+1):
    x, y, d = map(int, input().split())
    piece[x-1][y-1].append(i)
    now.append([x-1, y-1, d])


turn = 1
while True:
    if turn > 1000:
        break
    check = False
    for p in range(1, k+1):
        num = move(p)
        if num >= 4:
            check = True
            break
    if check:
        break
    turn += 1

if turn > 1000:
    print(-1)
else:
    print(turn)
