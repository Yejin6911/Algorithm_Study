import sys
import copy
input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
order = []
for i in range(t):
    x, d, k = map(int, input().rstrip().split())
    order.append((x, d, k))


# 회전
def spin(x, d, k):
    if d == 0:
        for i in range(x, n+1, x):
            for _ in range(k):
                temp = board[i-1].pop()
                board[i-1] = [temp]+board[i-1]
    else:
        for i in range(x, n+1, x):
            for _ in range(k):
                temp = board[i-1].pop(0)
                board[i-1].append(temp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def update():
    total = 0
    cnt = 0
    check = False
    new_board = copy.deepcopy(board)
    for x in range(n):
        total += sum(board[x])
        for y in range(m):
            if board[x][y]:
                cnt += 1
                now = board[x][y]
                # 인접한 부분 확인
                for i in range(4):
                    nx = x+dx[i]
                    ny = (y+dy[i]) % m
                    # 범위 벗어나는 경우 제외
                    if nx >= n or nx < 0:
                        continue
                    # 같으면 새로운 보드 0으로 변경
                    if board[nx][ny] == now:
                        new_board[nx][ny], new_board[x][y] = 0, 0
                        check = True
    # 같은 부분이 없으며 전체가 0이 아닐 떄
    if not check and cnt != 0:
        avg = total/cnt
        for x in range(n):
            for y in range(m):
                if board[x][y]:
                    if board[x][y] > avg:
                        new_board[x][y] -= 1
                    elif board[x][y] < avg:
                        new_board[x][y] += 1
    return new_board


for o in order:
    spin(o[0], o[1], o[2])
    board = update()

result = 0
for r in range(n):
    for c in range(m):
        result += board[r][c]

print(result)
