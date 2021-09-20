import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 동 서 남 북

n, m, x, y, k = map(int, input().split()) # 세로, 가로, 주사위x, 주사위y, 명령의 개수

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dice = [0 for _ in range(6)] # 위 북 동 서 남 아래
command = list(map(int, input().split())) # 이동 명령

for i in range(k):
    c = command[i] - 1
    nx = x + dx[c]
    ny = y + dy[c]
    if(not 0 <= nx < n or not 0 <= ny < m):
        continue
    
    if(c == 0): # 동쪽
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif(c == 1): #서쪽
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif(c == 2): # 북쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else: # 남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if(board[nx][ny] == 0):
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])