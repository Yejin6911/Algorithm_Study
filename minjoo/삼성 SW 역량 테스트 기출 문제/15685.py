import sys

input = sys.stdin.readline

n = int(input()) # 드래곤 커브의 개수
dc = [list(map(int, input().split())) for _ in range(n)] # 드래곤 커브의 정보
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 방향
board = [[0] * 101 for _ in range(101)] # 격자판

def makecurve(a, b, d, g): # 시작점, 방향, 세대
    global board
    x, y =  b, a
    cnt = 0
    action = [d]
    while(cnt < g):
        if(len(action) == 1):
            action.append((d+1)%4)
            cnt += 1
            continue
        temp2 = action[len(action)//2:]
        temp1 = []
        for a in action[:len(action)//2]:
            if(a < 2):
                temp1.append(a+2)
            else:
                temp1.append(a-2)
        action = action + temp1 + temp2
        cnt += 1
    
    board[x][y] = 1
    for i in range(len(action)):
        nx = x + dx[action[i]]
        ny = y + dy[action[i]]
        if(0<=nx<101 and 0<=ny<101):
            x, y = nx, ny
            board[x][y] = 1

for i in range(n):
    makecurve(dc[i][0], dc[i][1], dc[i][2], dc[i][3])

result = 0
for i in range(100):
    for j in range(100):
        if(board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1):
            result += 1
print(result)
    