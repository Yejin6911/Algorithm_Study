import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
shark = (n//2, n//2)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
step = [3, 2, 4, 1]


# 처음
def magic(d, s):
    x, y = shark[0], shark[1]
    # 구슬 파괴
    for i in range(s):
        x += dx[d]
        y += dy[d]
        board[x][y] = 0


# 0아닌 칸 순서대로 저장
def save():
    temp = []
    x, y = shark[0], shark[1]
    s = 0
    length = 1
    cnt = 0
    while True:
        if cnt == 2:
            length += 1
            cnt = 0
        if length >= n:
            for i in range(length-1):
                nx = x+dx[step[s]]
                ny = y+dy[step[s]]
                if board[nx][ny] != 0:
                    temp.append(board[nx][ny])
                x, y = nx, ny
            break
        for i in range(length):
            nx = x+dx[step[s]]
            ny = y+dy[step[s]]
            if board[nx][ny] != 0:
                temp.append(board[nx][ny])
            x, y = nx, ny
        cnt += 1
        # 방향 전환
        s = (s+1) % 4
    return temp


# 폭발
def explode(marble):
    global num
    check = True
    while check:
        start = 0
        now = 0
        cnt = 1
        new_marble = []
        check = False
        while True:
            if now >= len(marble)-1:
                break
            for i in range(now+1, len(marble)):
                if marble[now] == marble[i]:
                    cnt += 1
                else:
                    if cnt < 4:
                        now = i
                        cnt = 1
                        break
                    else:
                        check = True
                        num[marble[now]-1] += cnt
                        new_marble += marble[start:now]
                        start = i
                        now = i
                        cnt = 1
            if i == len(marble)-1:
                if cnt < 4:
                    now = i
                else:
                    num[marble[now]-1] += cnt
                    new_marble += marble[start:now]
                    start = i
                    now = i
                break
        for i in range(start, len(marble)):
            new_marble.append(marble[i])
        marble = new_marble
    return marble


def change(marble):
    new_marble = []
    i = 0
    while True:
        if i >= len(marble):
            break
        if i < len(marble)-1 and marble[i] == marble[i+1]:
            cnt = 1
            start = i+1
            while start < len(marble) and marble[start] == marble[i]:
                cnt += 1
                start += 1
            new_marble.extend([cnt, marble[i]])
            i += cnt
        else:
            new_marble.extend([1, marble[i]])
            i += 1
    if len(new_marble) > n*n:
        new_marble = new_marble[:n*n]
    elif len(new_marble) < n*n:
        for i in range(len(new_marble), n*n):
            new_marble.append(0)
    return new_marble


def update(marble):
    x, y = shark[0], shark[1]
    s = 0
    length = 1
    cnt = 0
    now = 0
    while True:
        if cnt == 2:
            length += 1
            cnt = 0
        if length >= n:
            for i in range(length-1):
                nx = x+dx[step[s]]
                ny = y+dy[step[s]]
                board[nx][ny] = marble[now]
                now += 1
                x, y = nx, ny
            break
        for i in range(length):
            nx = x+dx[step[s]]
            ny = y+dy[step[s]]
            board[nx][ny] = marble[now]
            now += 1
            x, y = nx, ny
        cnt += 1
        # 방향 전환
        s = (s+1) % 4


num = [0, 0, 0]
for _ in range(m):
    d, s = map(int, input().rstrip().split())
    magic(d, s)
    # 빈 칸 제외 순서대로 저장
    marble = save()
    marble = explode(marble)
    marble = change(marble)
    update(marble)

print(num[0]+2*num[1]+3*num[2])
