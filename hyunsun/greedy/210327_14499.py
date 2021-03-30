#똑똑한 move 아이디어 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#입력 
n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
#주사위 초기화
dice = [0 for _ in range(6)]

for i in range(k):
    dir = order[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < n or not 0 <= ny < m: #범위밖이면 무시 #continue
        continue

    #move 후에 윗면이 0, 아랫면이 5이도록 dice 계산
    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if a[nx][ny] == 0:
        a[nx][ny] = dice[5] #주사위 바닥의 숫자가 maps에 복사
    else:
        dice[5] = a[nx][ny] #maps의 숫자가 주사위 바닥에 복사
        a[nx][ny] = 0 #주의 : maps은 0

    x, y = nx, ny
    print(dice[0])

    
'''

#입력
n, m, x, y, k = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

#주사위 초기화
dice = [0 for _ in range(6)]
dice_space = 0

for i in range(k):
    if oreder[i] == 1:
        y += 1
        if y > m:
            #출력안하게
        else:
            dice_space =+ 1
            if map[x][y] == 0:
                map[x][y] = dice[dice_space] #주사위의 숫자가 여기에 복사
            else:
                dice[dice_space] = map[x][y]
                

'''

'''#똑똑한 move 아이디어
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#입력
n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
#주사위 초기화
dice = [0 for _ in range(6)]

for i in range(k):
    #dir = order[i] - 1 #효율적
    x += dx[order[i]-1] #nx 효율적
    y += dy[order[i]-1]
    
    if not 0 <= x < n or not 0 <= y < m:
        x -= dx[order[i]-1] #nx 효율적
        y -= dy[order[i]-1] 
        continue

    if order[i] == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif order[i] == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif order[i] == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if maps[x][y] == 0:
        maps[x][y] = dice[5]
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0

    print(dice[0])
'''
