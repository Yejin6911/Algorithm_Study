import copy
import sys
input = sys.stdin.readline

# 0:위, 1:아래, 2:왼쪽, 3:오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move():
    # check배열이 포인트
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, m+1):
        if shark[i] != 0:
            x, y, d = shark[i]
            direction = priority[i][d]
            flag = False
            for j in direction:
                nd = j
                nx = x+dx[nd]
                ny = y+dy[nd]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 비어있는 경우
                if board[nx][ny] == 0:
                    flag = True
                    break
            if not flag:
                for j in direction:
                    nd = j
                    nx = x+dx[nd]
                    ny = y+dy[nd]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny][0] == i:
                        break
        if check[nx][ny]:
            if check[nx][ny] < i:
                shark[i] = 0
            else:
                shark[check[nx][ny]] = 0
        else:
            check[nx][ny] = i
            shark[i] = [nx, ny, nd]


def update():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0


n, m, k = map(int, input().rstrip().split())
board = []  # [상어번호, 남은 초]
shark = [[] for _ in range(m+1)]  # [x,y,d]

for i in range(n):
    board.append(list(map(int, input().rstrip().split())))
    for j in range(n):
        if board[i][j]:
            shark[board[i][j]].extend([i, j])
            # 처음 뿌리기
            board[i][j] = [board[i][j], k]

shark_direction = list(map(int, input().rstrip().split()))
for i in range(m):
    shark[i+1].append(shark_direction[i]-1)

priority = [[] for _ in range(m+1)]
for i in range(1, m+1):
    for _ in range(4):
        temp = list(map(int, input().rstrip().split()))
        priority[i].append([x-1 for x in temp])

result = 0
while True:
    result += 1
    if result > 1000:
        print(-1)
        break
    # 이동
    move()
    update()

    # 상어 위치 update
    for i in range(1, m+1):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            board[x][y] = [i, k]

    if shark.count(0) == m-1:
        print(result)
        break
