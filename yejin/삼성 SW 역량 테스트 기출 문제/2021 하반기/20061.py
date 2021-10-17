blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]


def move(color, t, x, y):
    global green
    global blue
    # 초록색
    if color == 'g':
        if t == 1:
            block = [1, y]
            while True:
                if block[0]+1 == 6 or green[block[0]+1][block[1]]:
                    break
                else:
                    block[0] += 1
            green[block[0]][block[1]] = 1
        elif t == 2:
            block = [[1, y], [1, y+1]]
            while True:
                if (block[0][0]+1 == 6 or block[1][0] + 1 == 6):
                    break
                if green[block[0][0]+1][block[0][1]] or green[block[1][0]+1][block[1][1]]:
                    break
                else:
                    block[0][0] += 1
                    block[1][0] += 1
            green[block[0][0]][block[0][1]] = 1
            green[block[1][0]][block[1][1]] = 1
        else:
            block = [1, y]
            while True:
                if block[0]+1 == 6 or green[block[0]+1][block[1]]:
                    break
                else:
                    block[0] += 1
            green[block[0]][block[1]] = 1
            green[block[0]-1][block[1]] = 1
    # 파란색
    if color == 'b':
        if t == 1:
            block = [1, x]
            while True:
                if block[0]+1 == 6 or blue[block[0]+1][block[1]]:
                    break
                else:
                    block[0] += 1
            blue[block[0]][block[1]] = 1
        elif t == 2:
            block = [1, x]
            while True:
                if block[0]+1 == 6 or blue[block[0]+1][block[1]]:
                    break
                else:
                    block[0] += 1
            blue[block[0]][block[1]] = 1
            blue[block[0]-1][block[1]] = 1
        else:
            block = [[1, x], [1, x+1]]
            while True:
                if (block[0][0]+1 == 6 or block[1][0] + 1 == 6):
                    break
                if blue[block[0][0]+1][block[0][1]] or blue[block[1][0]+1][block[1][1]]:
                    break
                else:
                    block[0][0] += 1
                    block[1][0] += 1
            blue[block[0][0]][block[0][1]] = 1
            blue[block[1][0]][block[1][1]] = 1


def erase():
    global score
    global green
    global blue
    # 초록색
    r = 5
    while True:
        if r == 1:
            break
        if sum(green[r]) == 4:
            score += 1
            green.pop(r)
            green = [[0, 0, 0, 0]] + green
        else:
            r -= 1
    cnt = 0
    for i in range(2):
        if sum(green[i]) != 0:
            cnt += 1
    if cnt > 0:
        for _ in range(cnt):
            green.pop()
            green = [[0, 0, 0, 0]] + green
    # 파란색
    r = 5
    while True:
        if r == 1:
            break
        if sum(blue[r]) == 4:
            score += 1
            blue.pop(r)
            blue = [[0, 0, 0, 0]] + blue
        else:
            r -= 1
    cnt = 0
    for i in range(2):
        if sum(blue[i]) != 0:
            cnt += 1
    if cnt > 0:
        for _ in range(cnt):
            blue.pop()
            blue = [[0, 0, 0, 0]] + blue


n = int(input())
score = 0
cnt = 0
for _ in range(n):
    t, x, y = map(int, input().rstrip().split())
    move('g', t, x, y)
    move('b', t, x, y)
    erase()
for i in range(2, 6):
    for j in range(4):
        if green[i][j]:
            cnt += 1
        if blue[i][j]:
            cnt += 1
print(score)
print(cnt)
