import sys
input = sys.stdin.readline


def spin(d):
    global now_d
    # 오른쪽 회전
    if d == 'D':
        now_d = (now_d+1) % 4
    # 왼쪽 회전
    else:
        now_d = ((now_d-1)+4) % 4


def move(snake, d):
    head = snake[-1]
    nx = head[0]+dir[d][0]
    ny = head[1]+dir[d][1]
    # 자기 몸에 부딪히거나 벽에 부딪힌 경우
    if (nx, ny) in snake or nx in [0, N+1] or ny in [0, N+1]:
        return False
    else:
        snake.append((nx, ny))
        # 사과인 경우
        if board[nx][ny]:
            board[nx][ny] = 0
        else:
            # 몸길이 줄이기
            snake.pop(0)
        return True


N = int(input())
K = int(input())

board = [[0]*(N+2) for _ in range(N+2)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

# 뱀의 위치 저장 배열
snake = [(1, 1)]

L = int(input())
data = {}
for _ in range(L):
    x, c = input().split()
    data[int(x)] = c

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
now_d = 0

while True:
    # 뱀 이동
    time += 1
    check = move(snake, now_d)
    # 방향 변환 시점인 경우
    if time in data.keys():
        spin(data[time])
    # 게임 종료 여부 판별
    if check == False:
        break

print(time)
