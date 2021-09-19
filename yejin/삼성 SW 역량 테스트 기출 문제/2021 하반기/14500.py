import sys
input = sys.stdin.readline

tetrominos = [
    # -모양
    ([0, 0], [0, 1], [0, 2], [0, 3]),
    ([0, 0], [1, 0], [2, 0], [3, 0]),
    # ㅁ모양
    ([0, 0], [0, 1], [1, 1], [1, 0]),
    # ㄴ모양
    ([0, 0], [1, 0], [1, 1], [1, 2]),
    ([0, 0], [0, 1], [1, 0], [2, 0]),
    ([0, 0], [0, 1], [0, 2], [1, 2]),
    ([0, 1], [1, 1], [2, 1], [2, 0]),
    ([0, 0], [0, 1], [1, 1], [2, 1]),
    ([1, 0], [1, 1], [1, 2], [0, 2]),
    ([0, 0], [1, 0], [2, 0], [2, 1]),
    ([0, 0], [1, 0], [0, 1], [0, 2]),
    # ㄱㄴ모양
    ([0, 0], [1, 0], [1, 1], [2, 1]),
    ([1, 0], [1, 1], [0, 1], [0, 2]),
    ([2, 0], [1, 0], [1, 1], [0, 1]),
    ([0, 0], [0, 1], [1, 1], [1, 2]),
    # ㅜ 모양
    ([0, 0], [0, 1], [1, 1], [0, 2]),
    ([1, 0], [0, 1], [1, 1], [2, 1]),
    ([1, 0], [1, 1], [1, 2], [0, 1]),
    ([0, 0], [1, 0], [1, 1], [2, 0])
]


def getTotal(x, y, t):
    total = 0
    for i in range(4):
        nx = x + t[i][0]
        ny = y + t[i][1]
        # 종이 벗어나는 경우
        if 0 <= nx < n and 0 <= ny < m:
            total += board[nx][ny]
        else:
            return 0, False
    return total, True


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for t in tetrominos:
    for i in range(n):
        for j in range(m):
            total, check = getTotal(i, j, t)
            if check:
                answer = max(answer, total)
print(answer)
