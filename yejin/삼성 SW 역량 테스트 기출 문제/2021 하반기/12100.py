import sys
import copy
input = sys.stdin.readline


def move(board, d):
    # 상
    if d == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][j] = temp
    # 하
    elif d == 1:
        for j in range(n):
            idx = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = temp
    # 좌
    elif d == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = temp
    # 우
    else:
        for i in range(n):
            idx = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = temp


def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    temp = copy.deepcopy(board)
    for i in range(4):
        move(board, i)
        dfs(board, cnt + 1)
        # 보드 초기화
        board = copy.deepcopy(temp)


n = int(sys.stdin.readline().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(board, 0)
print(answer)
