import sys
import copy
input = sys.stdin.readline


def spin(x, d, k):
    for i in range(x, n+1, x):
        if d == 0:
            for _ in range(k):
                temp = board[i].pop()
                board[i] = [temp] + board[i]
        else:
            for _ in range(k):
                temp = board[i].pop(0)
                board[i].append(temp)


def erase():
    change = False
    total = 0
    cnt = 0
    new_board = copy.deepcopy(board)
    for i in range(1, n+1):
        total += sum(board[i])
        cnt += (m-board[i].count(0))
        for j in range(m):
            check = False
            if board[i][j]:
                # 인접하는 부분 중 같은 수 제거
                if board[i][j-1] == board[i][j]:
                    new_board[i][j-1] = 0
                    check = True
                if board[i][(j+1) % m] == board[i][j]:
                    new_board[i][(j+1) % m] = 0
                    check = True
                if i+1 <= n and board[i+1][j] == board[i][j]:
                    new_board[i+1][j] = 0
                    check = True
                if i-1 > 0 and board[i-1][j] == board[i][j]:
                    new_board[i-1][j] = 0
                    check = True
            if check:
                new_board[i][j] = 0
                change = True
    # 같은 수 없는 경우
    if not change and cnt != 0:
        avg = total/cnt
        for i in range(1, n+1):
            for j in range(m):
                if 0 < board[i][j] < avg:
                    new_board[i][j] += 1
                elif board[i][j] > avg:
                    new_board[i][j] -= 1
    return new_board


# n:원판의 개수, m: 원판에 적힌 수 개수
n, m, t = map(int, input().split())
board = [[]]
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
for _ in range(t):
    x, d, k = map(int, input().split())
    spin(x, d, k)
    board = erase()

total = 0
for row in board[1:]:
    total += sum(row)

print(total)
