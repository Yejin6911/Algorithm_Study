import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 자리배치
board = [[0]*n for _ in range(n)]
# 학생 순서
S = []
# 좋아하는 학생 목록
L = [[] for _ in range(n*n+1)]
for _ in range(n*n):
    data = list(map(int, input().rstrip().split()))
    S.append(data[0])
    L[data[0]].extend(data[1:])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def select(s):
    # (좋아하는 학생, 인접한 빈칸, 행, 열)
    now = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                like, empty = 0, 0
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0:
                            empty += 1
                        elif board[nx][ny] in L[s]:
                            like += 1
                now.append((like, empty, x, y))
    now.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return now[0][2], now[0][3]


for s in S:
    x, y = select(s)
    board[x][y] = s

result = 0
for x in range(n):
    for y in range(n):
        like = 0
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in L[board[x][y]]:
                like += 1
        if like > 0:
            result += (10**(like-1))
print(result)
