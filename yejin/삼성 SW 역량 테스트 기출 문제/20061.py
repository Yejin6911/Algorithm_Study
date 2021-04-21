import sys
input = sys.stdin.readline

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]


def put(t, x, y):
    b, g = False, False
    # 1X1
    if t == 1:
        for i in range(6):
            if not b:
                if blue[x][i] == 0:
                    if i == 5:
                        blue[x][i] = 1
                        b = True
                else:
                    blue[x][i-1] = 1
                    b = True
            if not g:
                if green[i][y] == 0:
                    if i == 5:
                        green[i][y] = 1
                        g = True
                else:
                    green[i-1][y] = 1
                    g = True
            if b and g:
                break
    # 1X2
    elif t == 2:
        for i in range(6):
            if not b:
                if blue[x][i] == 0:
                    if i == 5:
                        blue[x][i] = 1
                        blue[x][i-1] = 1
                        b = True
                else:
                    blue[x][i-1] = 1
                    blue[x][i-2] = 1
                    b = True
            if not g:
                if green[i][y] == 0 and green[i][y+1] == 0:
                    if i == 5:
                        green[i][y] = 1
                        green[i][y+1] = 1
                        g = True
                else:
                    green[i-1][y] = 1
                    green[i-1][y+1] = 1
                    g = True
            if b and g:
                break
    # 2X1
    else:
        for i in range(6):
            if not b:
                if blue[x][i] == 0 and blue[x+1][i] == 0:
                    if i == 5:
                        blue[x][i] = 1
                        blue[x+1][i] = 1
                        b = True
                else:
                    blue[x][i-1] = 1
                    blue[x+1][i-1] = 1
                    b = True
            if not g:
                if green[i][y] == 0:
                    if i == 5:
                        green[i][y] = 1
                        green[i-1][y] = 1
                        g = True
                else:
                    green[i-1][y] = 1
                    green[i-2][y] = 1
                    g = True
            if b and g:
                break


def domino():
    global score
    # 파란색 보드
    for y in range(2, 6):
        # 꽉 찬 열 있는 경우
        if blue[0][y]+blue[1][y]+blue[2][y]+blue[3][y] == 4:
            score += 1
            # 앞부분 이동
            for j in range(y, 0, -1):
                blue[0][j], blue[1][j], blue[2][j], blue[3][j] = blue[0][j -
                                                                         1], blue[1][j-1], blue[2][j-1], blue[3][j-1]
            blue[0][0], blue[1][0], blue[2][0], blue[3][0] = 0, 0, 0, 0
    # 0,1 열 확인
    cnt = 0
    for j in range(2):
        if blue[0][j]+blue[1][j]+blue[2][j]+blue[3][j] > 0:
            cnt += 1
    # 옆으로 이동
    for _ in range(cnt):
        for j in range(5, 0, -1):
            blue[0][j], blue[1][j], blue[2][j], blue[3][j] = blue[0][j -
                                                                     1], blue[1][j-1], blue[2][j-1], blue[3][j-1]
        blue[0][0], blue[1][0], blue[2][0], blue[3][0] = 0, 0, 0, 0

    # 초록색 보드
    for x in range(2, 6):
        # 꽉 찬 행 있는 경우
        if sum(green[x]) == 4:
            score += 1
            # 앞부분 이동
            for i in range(x, 0, -1):
                green[i] = green[i-1]
            green[0] = [0, 0, 0, 0]
    # 0,1 행 확인
    cnt = 0
    for i in range(2):
        if sum(green[i]) > 0:
            cnt += 1
    # 아래로 이동
    for _ in range(cnt):
        for i in range(5, 0, -1):
            green[i] = green[i-1]
        green[0] = [0, 0, 0, 0]


n = int(input().rstrip())
score = 0
result = 0
for _ in range(n):
    t, x, y = map(int, input().rstrip().split())
    put(t, x, y)
    domino()

for i in range(4):
    for j in range(6):
        if blue[i][j]:
            result += 1
        if green[j][i]:
            result += 1
print(score)
print(result)
