import sys
input = sys.stdin.readline

n = int(input())
block = [list(map(int, input().split())) for _ in range(n)]

blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]

score = 0

def greendraw(t, x, y):
    flag = 1
    if(t == 1):
        for i in range(6):
            if(green[i][y] != 0):
                green[i-1][y] = 1
                flag = 0
                break
        if(i == 5 and flag):
            green[i][y] = 1
    elif(t == 2):
        for i in range(6):
            if(green[i][y] != 0 or green[i][y+1] != 0):
                green[i-1][y] = 1
                green[i-1][y+1] = 1
                flag = 0
                break
        if(i == 5 and flag):
            green[i][y] = 1
            green[i][y+1] = 1
    elif(t == 3):
        for i in range(6):
            if(green[i][y] != 0):
                green[i-1][y] = 1
                green[i-2][y] = 1
                flag = 0
                break
        if(i == 5 and flag):
            green[i][y] = 1
            green[i-1][y] = 1
                
def bluedraw(t, x, y):
    flag = 1
    if(t == 1):
        for i in range(6):
            if(blue[i][3-x] != 0):
                blue[i-1][3-x] = 1
                flag = 0
                break
        if(i == 5 and flag):
            blue[i][3-x] = 1
    elif(t == 2):
        for i in range(6):
            if(blue[i][3-x] != 0):
                blue[i-1][3-x] = 1
                blue[i-2][3-x] = 1
                flag = 0
                break
        if(i == 5 and flag):
            blue[i][3-x] = 1
            blue[i-1][3-x] = 1
    elif(t == 3):
        for i in range(6):
            if(blue[i][3-x] != 0 or blue[i][2-x] != 0):
                blue[i-1][3-x] = 1
                blue[i-1][2-x] = 1
                flag = 0
                break
        if(i == 5 and flag):
            blue[i][3-x] = 1
            blue[i][2-x] = 1

def delete(board):
    global score
    for i in range(2, 6):
        if(not(0 in board[i])): # 다 1이면
            board.pop(i)
            board.insert(0, [0, 0, 0, 0])
            score += 1

    for i in range(2):
        if(1 in board[i]):
            board.pop()
            board.insert(0, [0, 0, 0, 0])

for i in range(n):
    t, x, y = block[i]
    greendraw(t, x, y)
    bluedraw(t, x, y)
    
    delete(green)
    delete(blue)

cnt = 0
for i in range(6):
    for j in range(4):
        if(green[i][j] == 1):
            cnt += 1
        if(blue[i][j] == 1):
            cnt += 1

print(score)
print(cnt)
