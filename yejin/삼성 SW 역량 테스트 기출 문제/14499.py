import sys

n, m, x, y, k = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

orders = sys.stdin.readline().rstrip().split()
orders = [int(x) for x in orders]

dice = [[0], [0, 0, 0], [0], [0]]
dx = [0, 0, -1, +1]
dy = [1, -1, 0, 0]

# 주사위 이동 가능 여부 확인


def check(x, y):
    x += dx[order-1]
    y += dy[order-1]
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    return True

# 주사위 회잔


def change_dice(order):
    # 동
    if order == 1:
        temp1 = dice[1][0]
        temp2 = dice[1][1]
        temp3 = dice[1][2]
        dice[1][0] = dice[3][0]
        dice[1][1] = temp1
        dice[1][2] = temp2
        dice[3][0] = temp3
    # 서
    elif order == 2:
        temp1 = dice[1][0]
        temp2 = dice[1][1]
        temp3 = dice[1][2]
        dice[1][2] = dice[3][0]
        dice[3][0] = temp1
        dice[1][0] = temp2
        dice[1][1] = temp3
    # 북
    elif order == 3:
        temp1 = dice[0][0]
        temp2 = dice[1][1]
        temp3 = dice[2][0]
        dice[2][0] = dice[3][0]
        dice[3][0] = temp1
        dice[0][0] = temp2
        dice[1][1] = temp3
    # 남
    else:
        temp1 = dice[0][0]
        temp2 = dice[1][1]
        temp3 = dice[2][0]
        dice[0][0] = dice[3][0]
        dice[1][1] = temp1
        dice[2][0] = temp2
        dice[3][0] = temp3

    return


# 주사위 이동 함수
def move(order):
    global x
    global y
    if check(x, y):
        x += dx[order-1]
        y += dy[order-1]
        change_dice(order)
        if map[x][y] == 0:
            map[x][y] = dice[3][0]
        else:
            dice[3][0] = map[x][y]
            map[x][y] = 0
        print(dice[1][1])
    return


# 명령 순서대로 실행
for order in orders:
    move(order)
